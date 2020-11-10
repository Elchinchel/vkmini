import asyncio
from copy import deepcopy
from typing import Union, Any

from .utils import AbstractLogger
from .method_groups import method_groups, MethodGroup
from .exceptions import VkResponseException, TokenInvalid, TooManyRequests
from .request import post

_loop = asyncio.get_event_loop()


def set_loop(loop: asyncio.AbstractEventLoop) -> None:
    global _loop
    _loop = loop


class VkApi:
    url: str = 'https://api.vk.com/method/'
    version: str
    access_token: str
    logger: Union[AbstractLogger, None]

    excepts: bool
    retries: int
    sync: bool

    __query: str

    def __new__(cls,
                access_token: str,
                excepts: bool = False,
                version: str = "5.110",
                retries: int = 0,
                sync_mode: bool = False,
                logger: AbstractLogger = None):
        if sync_mode:
            cls = VkApiSync
        instance = object.__new__(cls)
        instance.__init__(access_token, excepts, version,
                          retries, sync_mode, logger)
        return instance

    def __init__(self,
                 access_token: str,
                 excepts: bool = False,
                 version: str = "5.110",
                 retries: int = 0,
                 sync_mode: bool = False,
                 logger: AbstractLogger = None):
        """
        `retries` -- количество повторных попыток при возникновении ошибки
        TooManyRequests

        `sync_mode` -- если ложь, обращения к API будут возвращать awaitable
        корутины

        `excepts` -- генерировать ли VkResponseException при ошибках VK

        `logger` - любой объект, имеющий атрибуты info, debug и warning,
        по умолчанию None, то есть логирование не ведется
        """
        self._set_query(version, access_token)
        self.sync = sync_mode
        self.retries = retries
        self.logger = logger
        self.excepts = excepts
        for group in method_groups:
            setattr(self, group, MethodGroup(group, self))

    def _set_query(self, version: str, access_token: str):
        self.access_token, self.version = access_token, version
        self.__query = f'?v={version}&access_token={access_token}&lang=ru'

    async def _method(self, method: str, **kwargs) -> Any:
        if self.logger:
            self.logger.debug(
                f'URL = "{self.url}{method}{self.__query}" Data = {kwargs}'
            )
        resp_body = await post(self.url+method+self.__query, kwargs,
                               self.excepts)
        if 'response' in resp_body.keys():
            if self.logger:
                self.logger.info(f"Запрос {method} выполнен")
            return resp_body['response']
        elif 'error' in resp_body.keys():
            if self.logger:
                self.logger.warning(
                    f"Запрос {method} не выполнен: {resp_body['error']}"
                )
            if self.excepts:
                if resp_body['error']['error_code'] == 5:
                    raise TokenInvalid(resp_body['error'], kwargs)
                if resp_body['error']['error_code'] == 6:
                    raise TooManyRequests(resp_body["error"], kwargs)
                else:
                    raise VkResponseException(resp_body["error"], kwargs)
        return resp_body

    async def __tmr_retryer(self, method: str, **kwargs) -> Any:
        retry = 0
        while True:
            try:
                return await self._method(method, **kwargs)
            except VkResponseException as e:
                if e.error_code != 6 or retry == self.retries:
                    raise e
                await asyncio.sleep(0.5)
                retry += 1

    async def __call__(self, method, **kwargs) -> Any:
        return await self.__tmr_retryer(method, **kwargs)

    def __getattr__(self, name: str) -> MethodGroup:
        return MethodGroup(name, self)

    def sync_call(self, method: str, **kwargs) -> Any:
        if not _loop.is_running():
            return _loop.run_until_complete(
                self.__tmr_retryer(method, **kwargs)
            )
        else:
            return asyncio.run_coroutine_threadsafe(
                self.__tmr_retryer(method, **kwargs), _loop
            ).result()


class VkApiSync(VkApi):
    def __call__(self, method: str, **kwargs) -> Any:
        return self.sync_call(method, **kwargs)
