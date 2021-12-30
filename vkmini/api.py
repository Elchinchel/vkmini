import asyncio
from typing import Union, Any

from aiohttp.client import ClientSession

from .method_groups import method_groups, MethodGroup
from .exceptions import (
    VkResponseException, TokenInvalid, TooManyRequests, CaptchaNeeded
)
from .request import post
from .utils import AbstractLogger, run_coro_sync

_loop = asyncio.get_event_loop()


def set_loop(loop: asyncio.AbstractEventLoop) -> None:
    global _loop
    _loop = loop


class VkApi:
    url: str = 'https://api.vk.com/method/'
    user_id: Union[int, None] = None
    version: str
    access_token: str
    logger: Union[AbstractLogger, None]

    sync: bool
    retries: int
    excepts: bool

    __query: str
    __session: ClientSession = None

    def __new__(cls, *args, **kwargs):
        if 'sync_mode' in kwargs:
            cls = VkApiSync
        elif len(args) >= 5:
            if args[4]:
                cls = VkApiSync
        instance = object.__new__(cls)
        instance.__init__(*args, **kwargs)
        return instance

    def __init__(self,
                 access_token: str,
                 excepts: bool = False,
                 version: str = "5.110",
                 retries: int = 0,
                 sync_mode: bool = False,
                 logger: AbstractLogger = None,
                 session: ClientSession = None):
        """
        `retries` -- количество повторных попыток при возникновении ошибки
        TooManyRequests

        `sync_mode` -- если ложь, обращения к API будут возвращать awaitable
        корутины

        `excepts` -- генерировать ли VkResponseException при ошибках VK

        `logger` -- любой объект, имеющий атрибуты info, debug и warning,
        по умолчанию None, то есть логирование не ведется

        `session` -- aiohttp.ClientSession, см. описание vkmini.set_session
        """
        self._set_query(version, access_token)
        self.excepts = excepts
        self.retries = retries
        self.sync = sync_mode
        self.logger = logger
        if session is not None:
            self._session = session
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
        resp_body = await post(
            self.url+method+self.__query,
            kwargs,
            self.__session
        )
        if 'response' in resp_body.keys():
            if self.logger:
                self.logger.debug(f"Запрос {method} выполнен")
            return resp_body['response']
        elif 'error' in resp_body.keys():
            if self.logger:
                self.logger.warning(
                    f"Запрос {method} не выполнен: {resp_body['error']}"
                )
            if self.excepts:
                if resp_body['error']['error_code'] == 5:
                    raise TokenInvalid(resp_body['error'], kwargs)
                elif resp_body['error']['error_code'] == 6:
                    raise TooManyRequests(resp_body["error"], kwargs)
                elif resp_body['error']['error_code'] == 14:
                    raise CaptchaNeeded(resp_body["error"], kwargs)
                else:
                    raise VkResponseException(resp_body["error"], kwargs)
        return resp_body

    async def __retryer(self, method: str, **kwargs) -> Any:
        retry = 0
        while True:
            try:
                return await self._method(method, **kwargs)
            except VkResponseException as e:
                if e.error_code not in {6} or retry == self.retries:
                    raise e
                if e.error_code == 6:
                    await asyncio.sleep(0.5)
                # elif e.error_code == 14:
                #     if self.captcha_solver is None:
                #         raise e
                #     key = await self.captcha_solver.solve(e.error_data["captcha_img"])
                #     if key is None:
                #         raise e
                #     kwargs.update({
                #         "captcha_sid": e.error_data["captcha_sid"],
                #         "captcha_key": key
                #     })
                retry += 1

    async def __call__(self, method, **kwargs) -> Any:
        return await self.__retryer(method, **kwargs)

    async def set_user_id(self, user_id: Union[int, None] = None) -> None:
        if user_id is None:
            self.user_id = (await self.users.get())[0]["id"]
        self.user_id = user_id

    def __getattr__(self, name: str) -> MethodGroup:
        return MethodGroup(name, self)

    def sync_call(self, method: str, **kwargs) -> Any:
        return run_coro_sync(self.__retryer(method, **kwargs), _loop)


class VkApiSync(VkApi):
    def __call__(self, method: str, **kwargs) -> Any:
        return self.sync_call(method, **kwargs)
