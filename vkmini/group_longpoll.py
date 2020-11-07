from typing import AsyncGenerator, List, Union, Any

from .utils import AbstractLogger
from .request import longpoll_get
from .exceptions import TokenInvalid
from . import VkApi


class Update:

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


class LPGroup():
    make_classes: bool

    group_id: int
    server: str
    wait: int
    key: str
    ts: int

    time: float
    vk: VkApi

    def __init__(self, vk: VkApi, group_id: int, wait: int, make_classes: bool):
        'Для создания экземпляра используйте метод `new`'
        self.vk = vk
        self.wait = wait
        self.group_id = group_id
        self.make_classes = make_classes

    @staticmethod
    async def new(vk: VkApi, group_id: int, wait: int = 25,
                  make_classes: bool = True,
                  logger: AbstractLogger = None) -> "LPGroup":
        lp = LPGroup(vk, group_id, wait, make_classes)
        lp.logger = logger or vk.logger
        data = await vk('groups.getLongPollServer', group_id=group_id)
        if data.get('error'):
            if data['error']['error_code'] == 5:
                raise TokenInvalid
        lp.server = data['server']
        lp.key = data['key']
        lp.ts = data['ts']
        return lp

    @property
    async def check(self) -> List[Union[Update, List[Any]]]:
        'Возвращает список событий (updates)'
        data = await longpoll_get(
            f"{self.server}?act=a_check&key={self.key}&ts={self.ts}&wait={self.wait}",  # noqa
            self.vk.excepts
        )

        if 'failed' in data.keys():
            if data['failed'] == 1:
                if self.logger:
                    self.logger.warning('Ошибка истории событий')
                self.ts = data['ts']
            elif data['failed'] == 2:
                self.key = (await self.vk('groups.getLongPollServer',
                                          group_id=self.group_id))['key']
            else:
                if self.logger:
                    self.logger.error('Информация утрачена')
                data = await self.vk('groups.getLongPollServer',
                                     group_id=self.group_id)
                self.key = data['key']
                self.ts = data['ts']
            return []
        else:
            self.ts = data['ts']
            if self.make_classes:
                return [Update(update, self.vk) for update in data['updates']]
            else:
                return data['updates']

    async def listen(self) -> AsyncGenerator[Update, None]:
        while True:
            for update in await self.check:
                yield update
