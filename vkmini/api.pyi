from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Union, Any

from aiohttp.client import ClientSession

from vkmini.types import methods
from vkmini.utils import AbstractLogger
from vkmini.exceptions import VkResponseException, VkErrorCaptcha


class ExecuteResult:
    """Содержит результаты выполнения метода `execute`"""
    response: Any
    errors: List[VkResponseException]


class BaseCaptchaHandler(ABC):
    """
    Обработчик ошибки #14 (Captcha needed)

    Для обработки этой ошибки в конструктор класса `VkApi` необходимо
    передать объект, реализующий метод `solve_captcha`
    """
    RETRY_COUNT = 5

    @abstractmethod
    async def solve_captcha(self, error: VkErrorCaptcha) -> Optional[str]:
        """Возвращает строку -- решение капчи (captcha_key)"""
        raise NotImplementedError


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
    version: str
    lang: str
    access_token: str
    logger: Union[AbstractLogger, None]
    retries: int

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
            version: str = '5.131',
            retries: int = 0,
            logger: Optional[AbstractLogger] = None,
            session: Optional[ClientSession] = None,
            captcha_handler: Union[BaseCaptchaHandler, None] = None
    ):
        """
        `access_token` -- ключ доступа VK API
        (https://dev.vk.com/api/access-token/getting-started)

        `version` -- версия VK API (https://dev.vk.com/reference/versions)

        `retries` -- количество повторных попыток при возникновении ошибки
        TooManyRequests

        `logger` -- любой объект, имеющий атрибуты info, debug и warning,
        по умолчанию None, то есть логирование не ведется

        `session` -- aiohttp.ClientSession, см. описание `vkmini.set_session`

        `captcha_handler` -- экземпляр `vkmini.api.BaseCaptchaHandler`,
        используемый для обработки ошибки #14 (Captcha needed)
        """

    async def __call__(self, method: str, **kwargs) -> Any:
        """
        Выполняет вызов метода VK API

        `method` -- название метода, например 'messages.send'
        """

    async def execute(self, code: str) -> ExecuteResult:
        """
        Выполняет код на языке VKScript

        Описание метода: https://dev.vk.com/method/execute

        Возвращает объект `vkmini.api.ExecuteResult`
        """

    async def get_vk_id(self) -> int: ...

    async def wait_request_delay(self) -> None: ...

    async def _call_method(self, method: str, **kwargs) -> Any: ...

    async def _send_request(self, method: str, data: Dict[str, Any]) -> Dict[str, Any]: ...

    def _init_minimal(self, logger: Optional[AbstractLogger] = None, excepts: bool = False, session: Optional[ClientSession] = None, vk_id: Optional[int] = None): ...


class GroupVkApi(VkApi):
    """
    Класс для обращения к API с увеличенным количеством запросов в секунду
    """
