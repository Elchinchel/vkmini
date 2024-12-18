from abc import ABC, abstractmethod
from typing import Tuple, Callable, Optional, AsyncGenerator

from aiohttp.client import ClientSession

from vkmini import GroupVkApi, request


class LongPoller:
    __slots__ = ('server', 'key', 'ts', '_lp_data_getter')

    server: Optional[str]
    key: str
    ts: int

    def __init__(
            self,
            lp_data_getter,
            server_and_key: Optional[Tuple[str, str]] = None,
            ts: Optional[int] = None
    ) -> None:
        self.server = None
        self._lp_data_getter = lp_data_getter
        if server_and_key is not None:
            self.server, self.key = server_and_key
        if ts is not None:
            self.ts = ts

    async def _set_longpoll_data(self, *, new_ts: bool) -> None:
        data = await self._lp_data_getter()
        self.server = data['server']
        self.key = data['key']
        if new_ts:
            self.ts = data['ts']

    async def _handle_fail(self, data):
        if data['failed'] == 1:
            self.ts = data['ts']
        elif data['failed'] == 2:
            await self._set_longpoll_data(new_ts=False)
        else:
            await self._set_longpoll_data(new_ts=True)
        return []

    async def check(
            self,
            url_builder: 'Callable[[LongPoller], str]',
            session: Optional[ClientSession]
    ):
        if self.server is None:
            await self._set_longpoll_data(new_ts=(not hasattr(self, 'ts')))

        data = await request.get(url_builder(self), session)

        if 'failed' in data:
            return await self._handle_fail(data)
        else:
            self.ts = data['ts']
            return data['updates']


class BaseLP(ABC):
    _session: Optional[ClientSession]
    __session_owner: bool = False

    _poller: LongPoller

    @property
    def poller(self):
        return self._poller

    def set_poller(self, poller: LongPoller):
        self._poller = poller

    async def __aenter__(self):
        if self._session is None:
            self._session = ClientSession()
            self.__session_owner = True
        return self

    async def __aexit__(self, *_) -> None:
        if self.__session_owner and self._session is not None:
            await self._session.close()

    async def listen(self) -> AsyncGenerator[dict, None]:
        """
        Асинхронный генератор результатов метода check()
        """
        while True:
            for update in await self.check():
                yield update

    @abstractmethod
    async def check(self):
        raise NotImplementedError


class GroupLP(BaseLP):
    """
    Реализует получение событий через Bots Long Poll API
    (https://dev.vk.com/api/bots-long-poll/getting-started)
    """
    wait: int

    _vk: GroupVkApi
    _group_id: Optional[int]


    def __init__(
            self,
            vk: GroupVkApi,
            wait: int = 25,
            session: Optional[ClientSession] = None
    ):
        """
        Note:
            Приоритет объектов сессий:
            1. Сессия, переданная в параметре session
            2. Сессия переданного экземпляра VkApi

        Args:
            `wait`: максимальное время ожидания события, в секундах
                (https://dev.vk.com/api/bots-long-poll/getting-started#Подключение)

            `mode`: дополнительные опции ответа

            `session`: экземпляр aiohttp.ClientSession, который будет
                использоваться при выполнении запросов к LongPoll серверу
        """
        if not isinstance(vk, GroupVkApi):
            raise TypeError('Аргумент vk должен быть экземпляром %s, передан %s'
                            % GroupVkApi.__qualname__, repr(vk))

        self._vk = vk
        if wait > 90:
            raise ValueError('Параметр wait не может превышать 90 секунд')
        self.wait = wait
        self._session = session or vk._session  # type: ignore

        self._poller = LongPoller(self.get_longpoll_data)
        self._group_id = None

    async def check(self):
        """
        Выполняет однократный запрос к API и возвращает
        список событий из поля 'updates'
        (https://dev.vk.com/api/bots-long-poll/getting-started#Формат%20данных)
        """
        return await self._poller.check(self._get_url, self._session)

    def _get_url(self, poller: LongPoller):
        return (f"{poller.server}?act=a_check&key={poller.key}"
                f"&ts={poller.ts}&wait={self.wait}")

    async def get_longpoll_data(self):
        if self._group_id is None:
            self._group_id = await self._vk.get_vk_id()

        return await self._vk.groups.getLongPollServer(
            group_id=self._group_id
        )
