from typing import AsyncGenerator, Generator, List, Any, Union

from aiohttp.client import ClientSession

from .exceptions import TokenInvalid
from .request import longpoll_get
from .utils import AbstractLogger, run_coro_sync
from .api import VkApi, _loop


class LP:
    ts: int
    key: str
    server: str

    mode: int
    wait: int

    _vk: VkApi
    _pts: bool = False
    _session: Union[ClientSession, None]
    __session_owner: bool = True

    def __init__(self, vk: VkApi, wait: int = 25, mode: int = 2,
                 logger: AbstractLogger = None,
                 session: ClientSession = None) -> None:
        """
        Параметры `wait` и `mode` описаны в документации
        (https://vk.com/dev/using_longpoll)

        `logger` -- любой объект, имеющий атрибуты info, debug и warning,
        по умолчанию None, то есть логирование не ведется

        `session` -- экземпляр aiohttp.ClientSession, который будет
        использоваться при выполнении запросов к LongPoll серверу
        (при использовании класса в контексте, будет создана автоматически,
        иначе будет использоваться стандартная общая сессия,
        см. vkmini.set_default)

        Возвращает "сырой" класс, для подготовки к работе, нужно использовать
        его в контексте или вызвать метод `start`

        Пример с контекстом:
        ```
        async with LP(vk) as lp:
            print(await lp.check())
        ```
        Пример без контекста:
        ```
        lp = LP(vk)
        await lp.start()
        print(await lp.check())
        ```
        """
        self._init(vk, wait, mode, logger, session)

    def _init(self, vk, wait, mode, logger, session) -> None:
        self._vk = vk
        self.wait = wait
        self.mode = mode
        if self.mode & 32 == 32:
            self._pts = True
        self.logger = logger or vk.logger
        self._session = session
        if session is not None:
            self.__session_owner = False

    async def check(self) -> List[List[Any]]:
        data = await longpoll_get((
                f"https://{self.server}?act=a_check&key={self.key}"
                f"&ts={self.ts}&wait={self.wait}&mode={self.mode}&version=10"
            ), self._session)

        if 'failed' in data:
            if data['failed'] == 1:
                self.ts = data['ts']
            elif data['failed'] == 2:
                await self.get_longpoll_data(False)
            else:
                await self.get_longpoll_data(True)
            return []
        else:
            self.ts = data['ts']
            return data['updates']

    async def get_longpoll_data(self, new_ts: bool) -> None:
        data = await self._vk._method(
            'messages.getLongPollServer', need_pts=self._pts
        )
        if not self._vk.excepts:
            if data.get('error', {}).get('error_code') == 5:
                raise TokenInvalid(data['error'])
        self.server = data['server']
        self.key = data['key']
        if new_ts:
            self.ts = data['ts']

    async def start(self) -> None:
        await self.get_longpoll_data(True)

    async def __aenter__(self) -> "LP":
        if self._session is None:
            self._session = ClientSession()
            self.__session_owner = True
        await self.get_longpoll_data(True)
        return self

    async def __aexit__(self, *_) -> None:
        if self.__session_owner:
            await self._session.close()

    async def listen(self) -> AsyncGenerator[list, None]:
        """
        Возвращает асинхронный генератор LongPoll событий

        Официальная документация: https://vk.com/dev/using_longpoll_2
        """
        while True:
            for update in await self.check():
                yield update


class SyncLP(LP):
    # XXX: господи, кому вообще нужен синхронный поллер?
    def listen(self) -> Generator[list, None, None]:
        """
        Возвращает генератор LongPoll событий

        Официальная документация: https://vk.com/dev/using_longpoll_2
        """
        while True:
            for update in run_coro_sync(self.check(), _loop):
                yield update

    @staticmethod
    def new(vk: VkApi, wait: int = 25, mode: int = 2,
            logger: AbstractLogger = None,
            session: ClientSession = None) -> "SyncLP":
        lp = SyncLP(vk, wait, mode)
        if lp.mode & 32 == 32:
            lp._pts = True
        lp._session = session
        lp.logger = logger or vk.logger
        run_coro_sync(lp.get_longpoll_data(True), _loop)
        return lp
