import asyncio

from typing import Union, Any, Dict

from aiohttp.client import ClientSession

from vkmini.utils import AbstractLogger
from vkmini.request import post
from vkmini.exceptions import VkResponseException
from vkmini.method_groups import MethodGroup

_loop = asyncio.get_event_loop()


def set_loop(loop: asyncio.AbstractEventLoop) -> None:
    global _loop
    _loop = loop


class VkApi:
    URL: str = 'https://api.vk.com/method/%s?v=%s&lang=%s'
    rps_delay: int = 1 / 3

    user_id: Union[int, None] = None

    version: str
    lang: str = 'ru'

    access_token: str
    logger: Union[AbstractLogger, None]

    excepts: bool
    retries: int

    _sleep_lock: asyncio.Lock
    _session: ClientSession = None

    def __init__(
            self,
            access_token: str,
            excepts: bool = False,
            version: str = '5.130',
            retries: int = 0,
            sync_mode: bool = None,
            logger: AbstractLogger = None,
            session: ClientSession = None
    ):
        self.access_token = access_token
        self.excepts = excepts
        self.retries = retries
        self.version = version
        self.logger = logger
        self._session = session

        if retries > 0:
            self._sleep_lock = asyncio.Lock()

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

        try:
            response = resp_body['response']
        except KeyError:
            if self.logger:
                self.logger.warning(
                    f"Запрос {method} не выполнен: {resp_body['error']}"
                )
            if self.excepts:
                raise VkResponseException(resp_body['error'], kwargs) from None
            else:
                return resp_body['error']
        else:
            if self.logger:
                self.logger.debug(f"Запрос {method} выполнен")
            return response

    async def __retryer(self, method: str, **kwargs) -> Any:
        if self.retries == 0:
            return await self._call_method(method, **kwargs)

        retry = 0
        while True:
            try:
                if self._sleep_lock.locked():
                    async with self._sleep_lock:
                        return await self._call_method(method, **kwargs)

                return await self._call_method(method, **kwargs)
            except VkResponseException as e:
                if e.error_code not in {6} or retry == self.retries:
                    raise e from None
                if e.error_code == 6:
                    async with self._sleep_lock:
                        await asyncio.sleep(self.rps_delay)
                retry += 1

    async def __call__(self, method, **kwargs) -> Any:
        return await self.__retryer(method, **kwargs)

    async def get_user_id(self) -> int:
        if self.user_id is None:
            self.user_id = (await self.users.get())[0]['id']
        return self.user_id


class VkGroupApi(VkApi):
    rps_delay: int = 1 / 20

    async def get_user_id(self) -> int:
        if self.user_id is None:
            self.user_id = (await self.groups.getById())[0]['id']
        return self.user_id
