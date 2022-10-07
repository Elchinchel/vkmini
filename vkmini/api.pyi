import asyncio

from typing import Union, Any

from aiohttp.client import ClientSession

from vkmini.types import methods
from vkmini.utils import AbstractLogger


def set_loop(loop: asyncio.AbstractEventLoop) -> None:
    """
    Устанавливает цикл событий, который будет использоваться библиотекой
    """


class VkApi:
    """
    Класс для выполнения запросов к VK API

    Пример использования:
    ```
        vk = VkApi(access_token)

        conversation_list = await vk.messages.getConversations()
    ```
    """
    URL: str
    rps_delay: int
    user_id: Union[int, None]
    version: str
    lang: str
    access_token: str
    logger: Union[AbstractLogger, None]
    retries: int
    excepts: bool

    account: methods.account
    ads: methods.ads
    adsweb: methods.adsweb
    appWidgets: methods.appWidgets
    apps: methods.apps
    auth: methods.auth
    board: methods.board
    database: methods.database
    docs: methods.docs
    downloadedGames: methods.downloadedGames
    fave: methods.fave
    friends: methods.friends
    gifts: methods.gifts
    groups: methods.groups
    likes: methods.likes
    market: methods.market
    messages: methods.messages
    newsfeed: methods.newsfeed
    notes: methods.notes
    notifications: methods.notifications
    orders: methods.orders
    pages: methods.pages
    photos: methods.photos
    podcasts: methods.podcasts
    polls: methods.polls
    prettyCards: methods.prettyCards
    search: methods.search
    secure: methods.secure
    stats: methods.stats
    status: methods.status
    storage: methods.storage
    stories: methods.stories
    streaming: methods.streaming
    users: methods.users
    utils: methods.utils
    video: methods.video
    wall: methods.wall
    widgets: methods.widgets

    def __init__(
            self,
            access_token: str,
            excepts: bool = False,
            version: str = '5.131',
            retries: int = 0,
            sync_mode: bool = None,
            logger: AbstractLogger = None,
            session: ClientSession = None
    ):
        """
        `access_token` -- ключ доступа VK API
        (https://dev.vk.com/api/access-token/getting-started)

        `excepts` -- генерировать ли VkResponseException при ошибках VK API
        (иначе возвращает объект ошибки, полученный от VK)

        `version` -- версия VK API (https://dev.vk.com/reference/versions)

        `retries` -- количество повторных попыток при возникновении ошибки
        TooManyRequests

        `logger` -- любой объект, имеющий атрибуты info, debug и warning,
        по умолчанию None, то есть логирование не ведется

        `session` -- aiohttp.ClientSession, см. описание vkmini.set_session
        """

    async def __call__(self, method: str, **kwargs) -> Any:
        """
        Выполняет вызов метода VK API

        `method` -- название метода, например 'messages.send'
        """

    async def get_vk_id(self) -> int: ...


class GroupVkApi(VkApi):
    """
    Класс для обращения к API с увеличенным количеством запросов в секунду
    """
