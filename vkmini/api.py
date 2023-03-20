import asyncio

from abc import ABC, abstractmethod
from typing import List, Any, Dict, Optional, Union

from aiohttp.client import ClientSession

from vkmini import request
from vkmini.utils import AbstractLogger, Blocker, Version
from vkmini.exceptions import VkResponseException, VkErrorTooMany, VkErrorCaptcha
from vkmini.method_groups import MethodGroup


class ExecuteResult:
    response: Any
    errors: List[VkResponseException]

    def __init__(self, data: Dict[str, Any]) -> None:
        self.response = data['response']
        self.errors = [
            VkResponseException(err) for err in data.get('execute_errors', [])
        ]


class BaseCaptchaHandler(ABC):
    RETRY_COUNT = 5

    @abstractmethod
    async def solve_captcha(self, error: VkErrorCaptcha) -> Optional[str]:
        raise NotImplementedError


class VkApi:
    URL: str = 'https://api.vk.com/method/%s?v=%s&lang=%s'
    rps_delay: float = 1 / 3

    _vk_id: Union[int, None] = None

    version: str
    lang: str = 'ru'

    access_token: str
    logger: Union[AbstractLogger, None]

    retries: int

    _blocker: Blocker
    _session: Optional[ClientSession]
    _releaser: Optional[asyncio.Task]
    _captcha_handler: Optional[BaseCaptchaHandler]

    def __init__(
            self,
            access_token: str,
            version: str = '5.130',
            retries: int = 0,
            logger: Optional[AbstractLogger] = None,
            session: Optional[ClientSession] = None,
            captcha_handler: Union[BaseCaptchaHandler, None] = None
    ):
        self._init_minimal(logger, session)

        self.access_token = access_token
        assert isinstance(version, str), 'Параметр version должен иметь тип str'
        self.version = version
        self.retries = retries
        self._captcha_handler = captcha_handler

        if retries > 0:
            self._blocker = Blocker()
            self._releaser = None

    def _init_minimal(
            self,
            logger: Optional[AbstractLogger] = None,
            session: Optional[ClientSession] = None,
            vk_id: Optional[int] = None,
    ):
        self.logger = logger
        self._session = session
        if vk_id is not None:
            self._vk_id = vk_id

    def _set_method_groups(self):
        for group in MethodGroup._get_all(self):
            setattr(self, group.name, group)

    def __getattr__(self, name):
        if (group := MethodGroup._get(self, name)) is not None:
            return group
        raise AttributeError('No attribute \'%s\'' % name)

    async def _send_request(
            self,
            method: str,
            data: Dict[str, Any]
    ) -> Dict[str, Any]:
        data['access_token'] = self.access_token
        response = await request.post(
            self.URL % (method, self.version, self.lang),
            data,
            self._session
        )
        del(data['access_token'])
        return response

    async def _call_method(self, method: str, **kwargs) -> Any:
        if self.logger:
            self.logger.debug(f'API.{method}({kwargs})')

        resp_body = await self._send_request(method, kwargs)

        if 'response' in resp_body:
            if self.logger:
                self.logger.debug(f"Запрос {method} выполнен")
            return resp_body
        elif 'error' in resp_body:
            if self.logger:
                self.logger.warning(
                    f"Запрос {method} не выполнен: {resp_body['error']}"
                )
            raise VkResponseException(resp_body['error'], kwargs)

        raise ValueError('Неизвестный формат ответа VK API')

    async def __retryer(self, method: str, **kwargs) -> Any:
        if self.retries == 0:
            return await self._call_method(method, **kwargs)

        too_many_retry = captcha_retry = 0
        while True:
            if not self._blocker.is_allowed():
                await self._blocker.wait()
            try:
                return await self._call_method(method, **kwargs)
            except VkErrorTooMany as e:
                if too_many_retry == self.retries:
                    raise e from None
                self._blocker.block()
                self.__release_blocker()
                await self.wait_request_delay()
                too_many_retry += 1
            except VkErrorCaptcha as e:
                if not self._captcha_handler or \
                        captcha_retry == self._captcha_handler.RETRY_COUNT:
                    raise
                if (key := await self._captcha_handler.solve_captcha(e)) is None:
                    raise
                kwargs['captcha_key'] = key
                kwargs['captcha_sid'] = e.error_data['captcha_sid']

    def __release_blocker(self):
        if not self._releaser:
            blocker = self._blocker

            async def releaser():
                while not blocker.is_allowed():
                    await self.wait_request_delay()
                    blocker.release_one()
                self._releaser = None

            self._releaser = asyncio.create_task(releaser())

    async def __call__(self, method, **kwargs) -> Any:
        return (await self.__retryer(method, **kwargs))['response']

    async def execute(self, code: str) -> ExecuteResult:
        return ExecuteResult(await self.__retryer('execute', code=code))

    async def get_vk_id(self) -> int:
        if self._vk_id is None:
            self._vk_id = (await self.users.get())[0]['id']
        return self._vk_id

    async def get_user_id(self) -> int:
        return await self.get_vk_id()

    async def wait_request_delay(self):
        return await asyncio.sleep(self.rps_delay)


class GroupVkApi(VkApi):
    rps_delay: float = 1 / 20

    async def get_vk_id(self) -> int:
        if self._vk_id is None:
            if Version(self.version) >= Version('5.140'):
                self._vk_id = (await self.groups.getById())['groups'][0]['id']
            else:
                self._vk_id = (await self.groups.getById())[0]['id']
        return self._vk_id
