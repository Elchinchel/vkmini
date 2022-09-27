from typing import AsyncGenerator, List, Any, Union
from warnings import warn

from aiohttp.client import ClientSession

from vkmini.api import VkApi
from vkmini.utils import AbstractLogger
from vkmini.request import longpoll_get, _check_longpoll_session
from vkmini.exceptions import TokenInvalid


class LP:
    """
    Реализует получение событий через User Long Poll API

    Официальная документация:
    https://dev.vk.com/api/user-long-poll/getting-started

    Неофициальная документация:
    https://github.com/danyadev/longpoll-doc
    """
    ts: int
    key: str
    server: str

    mode: int
    wait: int

    _vk: VkApi
    _session: Union[ClientSession, None]
    __session_owner: bool = False

    def __init__(
            self,
            vk: VkApi,
            wait: int = 25,
            mode: int = 2,
            logger: AbstractLogger = None,
            session: ClientSession = None
        ):
        """
        `wait` -- максимальное время ожидания события, в секундах
        (https://dev.vk.com/api/user-long-poll/getting-started#Подключение)

        `mode` -- дополнительные опции ответа

        `logger` -- любой объект, имеющий атрибуты info, debug и warning,
        по умолчанию None, то есть логирование не ведется

        `session` -- экземпляр aiohttp.ClientSession, который будет
        использоваться при выполнении запросов к LongPoll серверу

        Приоритет объектов сессий:
        1. Сессия, переданная в параметре session
        2. Сессия переданного экземпляра VkApi
        3. Общая сессия (см vkmini.set_session)
        """
        self._init(vk, wait, mode, logger, session)

    def _init(self, vk, wait, mode, logger, session) -> None:
        self._vk = vk
        self.wait = wait
        self.mode = mode
        self.logger = logger or vk.logger
        self._session = session or vk._session

    async def check(self):
        """
        Выполняет однократный запрос к API и возвращает
        список событий из поля 'updates'
        (https://dev.vk.com/api/user-long-poll/getting-started#Формат%20ответа)
        """
        _check_longpoll_session(self._session)
        await self._set_longpoll_data(True)
        self.check = self._check
        return await self.check()

    async def _check(self) -> List[List[Any]]:
        data = await longpoll_get(
            f"https://{self.server}?act=a_check&key={self.key}"
            f"&ts={self.ts}&wait={self.wait}&mode={self.mode}&version=10",
            self._session
        )

        if 'failed' in data:
            if data['failed'] == 1:
                self.ts = data['ts']
            elif data['failed'] == 2:
                await self._set_longpoll_data(False)
            else:
                await self._set_longpoll_data(True)
            return []
        else:
            self.ts = data['ts']
            return data['updates']

    async def _set_longpoll_data(self, new_ts: bool) -> None:
        data = await self._vk.messages.getLongPollServer(
            need_pts=bool(self.mode & 32 == 32)
        )
        if not self._vk.excepts:
            if data.get('error', {}).get('error_code') == 5:
                raise TokenInvalid(data['error'])
        self.server = data['server']
        self.key = data['key']
        if new_ts:
            self.ts = data['ts']

    async def __aenter__(self) -> 'LP':
        if self._session is None:
            self._session = ClientSession()
            self.__session_owner = True
        return self

    async def __aexit__(self, *_) -> None:
        if self.__session_owner:
            await self._session.close()

    async def listen(self) -> AsyncGenerator[list, None]:
        """
        Асинхронный генератор результатов метода check()
        """
        while True:
            for update in await self.check():
                yield update
