import asyncio
from queue import Queue
from typing import Callable, Union, Any
from .utils import LoggerType, sync_wrapper
from .methods.method_group import MethodGroup
from .exceptions import VkResponseException, TokenInvalid, TooManyRequests
from .request import post

_loop = asyncio.get_event_loop()


def set_loop(loop: asyncio.AbstractEventLoop) -> None:
    global _loop
    _loop = loop


class VkApi:
    url: str = 'https://api.vk.com/method/'
    query: str
    logger: Union[Callable, None]

    excepts: bool
    retries: int
    sync: bool

    def __init__(self,
                 access_token: str,
                 excepts: bool = False,
                 version: str = "5.110",
                 retries: int = 5,
                 sync_mode: bool = False,
                 logger: LoggerType = None):
        """
        Eсли `excepts` == True, ошибки ВК будут генерировать
        исключение VkResponseException

        `logger` - любой объект, имеющий атрибуты info, debug и warning,
        по умолчанию None, то есть логирование не ведется
        """
        self._set_query(version, access_token)
        self.sync = sync_mode
        if self.sync:
            self.switch_to_sync()
        self.retries = retries
        self.logger = logger
        self.excepts = excepts
        self.messages = MethodGroup('messages', self)

    def _set_query(self, version: str, access_token: str):
        self.query = f'?v={version}&access_token={access_token}&lang=ru'

    async def _method(self, method: str, **kwargs) -> Any:
        if self.logger:
            self.logger.debug(f'URL = "{self.url}{method}{self.query}" Data = {kwargs}')
        resp_body = await post(f'{self.url}{method}{self.query}', kwargs, self.excepts)
        if 'response' in resp_body.keys():
            if self.logger:
                self.logger.info(f"Запрос {method} выполнен")
            return resp_body['response']
        elif 'error' in resp_body.keys():
            if self.logger:
                self.logger.warning(f"Запрос {method} не выполнен: {resp_body['error']}")
            if self.excepts:
                if resp_body['error']['error_code'] == 5:
                    raise TokenInvalid(resp_body['error'])
                if resp_body['error']['error_code'] == 6:
                    raise TooManyRequests(resp_body["error"], kwargs)
                else:
                    raise VkResponseException(resp_body["error"])
        return resp_body

    async def __tmr_retryer(self, method: str, **kwargs) -> Any:
        retry = 0
        while retry < self.retries:
            try:
                return await self._method(method, **kwargs)
            except VkResponseException as e:
                if e.error_code != 6:
                    raise e
                await asyncio.sleep(0.5)
                retry += 1

    async def __call__(self, method, **kwargs) -> Any:
        return await self.__tmr_retryer(method, **kwargs)

    def __getattr__(self, name: str) -> MethodGroup:
        return MethodGroup(name, self)

    def sync_call(self, method: str, **kwargs) -> Any:
        queue = Queue()
        if not _loop.is_running():
            _loop.run_until_complete(
                sync_wrapper(queue, self.__tmr_retryer(method, **kwargs))
            )
        else:
            _loop.create_task(
                sync_wrapper(queue, self.__tmr_retryer(method, **kwargs))
            )
        result, error = queue.get()
        if error is None:
            return result
        else:
            raise error

    def switch_to_sync(self) -> None:
        self.__call__ = self.sync_call
        self.sync = True
