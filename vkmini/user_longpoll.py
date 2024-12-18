from typing import Any, List, Generic, TypeVar, Optional

from aiohttp.client import ClientSession

from vkmini.api import VkApi
from vkmini.group_longpoll import BaseLP, LongPoller


PollerT = TypeVar('PollerT', bound=LongPoller)


class UserLP(BaseLP, Generic[PollerT]):
    """
    Реализует получение событий через User Long Poll API

    Официальная документация:
    https://dev.vk.com/api/user-long-poll/getting-started

    Неофициальная документация:
    https://github.com/danyadev/longpoll-doc
    """
    mode: int
    wait: int

    _vk: VkApi
    _poller: Optional[PollerT]

    def __init__(
            self,
            vk: VkApi,
            wait: int = 25,
            mode: int = 2,
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
        self._vk = vk
        self.wait = wait
        self.mode = mode

        self._session = session or vk._session  # type: ignore

        self._poller = None

    async def check(self) -> List[List[Any]]:
        """
        Выполняет однократный запрос к API и возвращает
        список событий из поля 'updates'
        (https://dev.vk.com/api/user-long-poll/getting-started#Формат%20ответа)
        """
        if self._poller is None:
            self.set_poller(LongPoller(self.get_longpoll_data))

        return await self._poller.check(self._get_url, self._session)  # pyright: ignore[reportOptionalMemberAccess]

    def _get_url(self, poller: LongPoller):
        return (f"https://{poller.server}?act=a_check&key={poller.key}"
                f"&ts={poller.ts}&wait={self.wait}&mode={self.mode}&version=10")

    async def get_longpoll_data(self):
        return await self._vk.messages.getLongPollServer(
            need_pts=int(self.mode & 32 == 32)
        )
