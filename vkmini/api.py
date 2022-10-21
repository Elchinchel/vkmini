import asyncio

from abc import ABC, abstractmethod
from typing import List, Any, Dict, Type, Optional, Union

from aiohttp.client import ClientSession

from vkmini.utils import AbstractLogger, Blocker
from vkmini.request import post
from vkmini.exceptions import VkResponseException, VkErrorTooMany, VkErrorCaptcha
from vkmini.method_groups import MethodGroup


def set_loop(loop):
    pass


class ExecuteResult:
    response: Optional[Any]
    errors: List[VkResponseException]

    def __init__(self, data: Dict[str, Any]) -> None:
        self.response = data.get('response')
        self.errors = [
            VkResponseException(err) for err in data.get('execute_errors', [])
        ]


class CaptchaHandler(ABC):
    RETRY_COUNT = 5

    @abstractmethod
    async def solve_captcha(self, error: VkErrorCaptcha) -> str:
        raise NotImplementedError


class VkApi:
    URL: str = 'https://api.vk.com/method/%s?v=%s&lang=%s'
    rps_delay: float = 1 / 3

    _vk_id: Union[int, None] = None

    version: str
    lang: str = 'ru'

    access_token: str
    logger: Union[AbstractLogger, None]

    excepts: bool
    retries: int

    _blocker: Blocker
    _session: ClientSession
    _releaser: asyncio.Task
    _captcha_handler: Optional[CaptchaHandler]

    def __init__(
            self,
            access_token: str,
            excepts: bool = False,
            version: str = '5.131',
            retries: int = 0,
            sync_mode: bool = None,
            logger: AbstractLogger = None,
            session: ClientSession = None,
            captcha_handler: Union[CaptchaHandler, None] = None
    ):
        self.access_token = access_token
        self.excepts = excepts
        self.version = version
        self.retries = retries
        self.logger = logger
        self._session = session
        self._captcha_handler = captcha_handler

        if retries > 0:
            self._blocker = Blocker(asyncio.get_event_loop().create_future)
            self._releaser = None

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
        response = await post(
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
            if self.excepts:
                raise VkResponseException(resp_body['error'], kwargs) from None
            return resp_body['error']

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
                    raise e from None
                kwargs['captcha_key'] = await self._captcha_handler.solve_captcha(e)
                kwargs['captcha_sid'] = e.error_data['captcha_sid']

    def __release_blocker(self):
        if not self._releaser:
            blocker = self._blocker
            wait_delay = self.wait_request_delay

            async def releaser():
                while not blocker.is_allowed():
                    await wait_delay()
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
            self._vk_id = (await self.groups.getById())[0]['id']
        return self._vk_id
