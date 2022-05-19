from typing import AsyncGenerator, Union

from aiohttp.client import ClientSession

from vkmini import VkApi
from vkmini.utils import AbstractLogger
from vkmini.request import longpoll_get, default_session


class GroupLP:
    wrap_events: bool

    group_id: int
    server: str
    wait: int
    key: str
    ts: int

    time: float
    vk: VkApi

    _session: Union[ClientSession, None]

    __session_owner: bool = False

    def __init__(self,
                 vk: VkApi,
                 wait: int = 25,
                 logger: AbstractLogger = None,
                 session: ClientSession = default_session) -> None:
        """
        Параметр `wait` описан в документации
        (https://vk.com/dev/bots_longpoll)

        `logger` -- любой объект, имеющий атрибуты info, debug и warning,
        по умолчанию None, то есть логирование не ведется

        `session` -- экземпляр aiohttp.ClientSession, который будет
        использоваться при выполнении запросов к LongPoll серверу
        (при использовании класса в контексте, будет создана автоматически,
        иначе будет использоваться стандартная общая сессия,
        см. vkmini.set_default)
        """
        vk.excepts = True
        self._vk = vk
        self.wait = wait
        self.logger = logger or vk.logger
        self._session = session

    async def check(self):
        self.group_id = (await self._vk.groups.getById())[0]['id']
        await self.get_longpoll_data(True)
        self.check = self._check
        return await self.check()

    async def _check(self):
        'Возвращает список событий (updates)'
        data = await longpoll_get(
            f"{self.server}?act=a_check&key={self.key}" +
            f"&ts={self.ts}&wait={self.wait}",
            self._session
        )

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
            'groups.getLongPollServer', group_id=self.group_id
        )
        self.server = data['server']
        self.key = data['key']
        if new_ts:
            self.ts = data['ts']

    async def __aenter__(self) -> "GroupLP":
        if self._session is None:
            self._session = ClientSession()
            self.__session_owner = True
        return self

    async def __aexit__(self, *_) -> None:
        if self.__session_owner:
            await self._session.close()

    async def listen(self) -> AsyncGenerator[dict, None]:
        while True:
            for update in await self.check():
                yield update
