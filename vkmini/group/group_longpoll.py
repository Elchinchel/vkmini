from typing import AsyncGenerator, List, Union, Any

from aiohttp.client import ClientSession

from vkmini.utils import AbstractLogger
from vkmini.request import longpoll_get
from vkmini.exceptions import TokenInvalid
from vkmini import VkApi


class Update:
    # TODO ну тут без комментариев
    class _Message:
        date: int
        from_id: int
        id: int
        out: int
        peer_id: int
        text: str
        conversation_message_id: int
        fwd_messages: list
        important: bool
        attachments: list
        is_hidden: bool
        client_info: dict
        reply_message: dict = None

        def __init__(self, object):
            self.__dict__.update(object)

    type: str
    object: dict
    message: _Message

    vk: VkApi

    def __init__(self, update, vk):
        self.vk = vk
        self.type = update['type']
        self.object = update['object']
        if self.type == 'message_new':
            self.message = self._Message(self.object['message'])

    def __getitem__(self, key):
        return self.object[key]

    async def reply_to_peer(self, message, **kwargs):
        return await self.vk.msg_op(1, self.message.peer_id, message, **kwargs)


class GroupLP:
    # TODO: чёт старовато капец
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

    def __init__(self, vk: VkApi, group_id: int, wait: int = 25,
                 logger: AbstractLogger = None,
                 session: ClientSession = None) -> None:
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

        Возвращает "сырой" класс, для подготовки к работе, нужно использовать
        его в контексте или вызвать метод `start`

        Пример с контекстом:
        ```
        async with GroupLP(vk, group_id) as lp:
            print(await lp.check())
        ```
        Пример без контекста:
        ```
        lp = GroupLP(vk, group_id)
        await lp.start()
        print(await lp.check())
        ```
        """
        self._vk = vk
        self.wait = wait
        self.group_id = group_id
        self.logger = logger or vk.logger
        self._session = session

    @property
    async def check(self) -> List[Union[Update, List[Any]]]:
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
            # if self.wrap_events:
            # return [Update(update, self.vk) for update in data['updates']]
            # else:
            return data['updates']

    async def get_longpoll_data(self, new_ts: bool) -> None:
        data = await self._vk._method(
            'groups.getLongPollServer', group_id=self.group_id
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

    async def __aenter__(self) -> "GroupLP":
        if self._session is None:
            self._session = ClientSession()
            self.__session_owner = True
        await self.get_longpoll_data(True)
        return self

    async def __aexit__(self, *_) -> None:
        if self.__session_owner:
            await self._session.close()

    async def listen(self) -> AsyncGenerator[Update, None]:
        while True:
            for update in await self.check:
                yield update
