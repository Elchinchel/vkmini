from typing import Optional, TypeVar, Generic, List, Any

from aiohttp.client import ClientSession

from vkmini.api import VkApi
from vkmini.utils import AbstractLogger
from vkmini.request import check_longpoll_session
from vkmini.group_longpoll import LongPoller, BaseLP


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
            logger: Optional[AbstractLogger] = None,
            session: Optional[ClientSession] = None
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
        self._vk = vk
        self.wait = wait
        self.mode = mode

        self.logger = logger or vk.logger
        self._session = session or vk._session  # type: ignore

        self._poller = None

    async def check(self) -> List[List[Any]]:
        """
        Выполняет однократный запрос к API и возвращает
        список событий из поля 'updates'
        (https://dev.vk.com/api/user-long-poll/getting-started#Формат%20ответа)
        """
        if self._poller is None:
            check_longpoll_session(self._session)
            self.set_poller(LongPoller(self.get_longpoll_data))

        return await self._poller.check(self._get_url, self._session)  # pyright: ignore[reportOptionalMemberAccess]

    def _get_url(self, poller: LongPoller):
        return (f"https://{poller.server}?act=a_check&key={poller.key}"
                f"&ts={poller.ts}&wait={self.wait}&mode={self.mode}&version=10")

    async def get_longpoll_data(self):
        return await self._vk.messages.getLongPollServer(
            need_pts=bool(self.mode & 32 == 32)
        )
