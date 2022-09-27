from typing import AsyncGenerator, Union

from aiohttp.client import ClientSession

from vkmini import VkApi
from vkmini.utils import AbstractLogger
from vkmini.request import longpoll_get, _check_longpoll_session


class GroupLP:
    """
    Реализует получение событий через Bots Long Poll API
    (https://dev.vk.com/api/bots-long-poll/getting-started)
    """
    wait: int
    group_id: int

    server: str
    key: str
    ts: int

    _vk: VkApi
    _session: Union[ClientSession, None]

    __session_owner: bool = False

    def __init__(
            self,
            vk: VkApi,
            group_id: int = None,
            wait: int = 25,
            logger: AbstractLogger = None,
            session: ClientSession = None
    ):
        """
        `wait` -- максимальное время ожидания события, в секундах
        (https://dev.vk.com/api/bots-long-poll/getting-started#Подключение)

        `logger` -- любой объект, имеющий атрибуты info, debug и warning,
        по умолчанию None, то есть логирование не ведется

        `session` -- экземпляр aiohttp.ClientSession, который будет
        использоваться при выполнении запросов к LongPoll серверу

        Приоритет объектов сессий:
        1. Сессия, переданная в параметре session
        2. Сессия переданного экземпляра VkApi
        3. Общая сессия (см vkmini.set_session)
        """
        self._vk = vk

        if wait > 90:
            raise ValueError('Параметр wait не может превышать 90 секунд')
        self.wait = wait
        self.logger = logger or vk.logger
        self._session = session or vk._session
        self.group_id = group_id

    async def check(self):
        """
        Выполняет однократный запрос к API и возвращает
        список событий из поля 'updates'
        (https://dev.vk.com/api/bots-long-poll/getting-started#Формат%20данных)
        """
        _check_longpoll_session(self._session)
        if self.group_id is None:
            self.group_id = await self._vk.get_user_id()
        await self._set_longpoll_data(True)
        self.check = self._check
        return await self.check()

    async def _check(self):
        data = await longpoll_get(
            f"{self.server}?act=a_check&key={self.key}" +
            f"&ts={self.ts}&wait={self.wait}",
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
        data = await self._vk.groups.getLongPollServer(
            group_id=self.group_id
        )
        self.server = data['server']
        self.key = data['key']
        if new_ts:
            self.ts = data['ts']

    async def __aenter__(self) -> 'GroupLP':
        if self._session is None:
            self._session = ClientSession()
            self.__session_owner = True
        return self

    async def __aexit__(self, *_) -> None:
        if self.__session_owner:
            await self._session.close()

    async def listen(self) -> AsyncGenerator[dict, None]:
        """
        Асинхронный генератор результатов метода check()
        """
        while True:
            for update in await self.check():
                yield update
