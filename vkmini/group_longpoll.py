"""
не работает по причине автор ленивая жопа (надо переделать под aio)
"""
import requests
from . import VkApi
from datetime import datetime

# from wtflog import warden
# logger = warden.get_boy('VK Group LongPoll')
from .printer import Printer
logger = Printer()

class LPGroup():
    key: str
    server:str
    ts: int
    group_id: int
    time: float
    vk: VkApi
    wait: int

    def __init__(self, vk, group_id, wait = 25):
        'vk - экземпляр VkApi'
        self.vk = vk
        self.group_id = group_id
        data = vk('groups.getLongPollServer', group_id = group_id)
        if data.get('error'):
            if data['error']['error_code'] == 5:
                raise Exception('Неверный токен')
        self.server = data['server']
        self.key = data['key']
        self.ts = data['ts']
        self.wait = wait

    @property
    def check(self):
        'Возвращает список событий (updates)'
        response = requests.get(f"{self.server}?act=a_check&key={self.key}&ts={self.ts}&wait={self.wait}")
        if response.status_code != 200:
            logger.error('Ошибка сети')
            return []

        self.time = datetime.now().timestamp()
        data = response.json()

        if 'failed' in data.keys():
            if data['failed'] == 1:
                logger.error('Ошибка истории событий')
                self.ts = data['ts']
            elif data['failed'] == 2:
                self.key = self.vk('groups.getLongPollServer', group_id = self.group_id)['key']
            else:
                logger.error('Информация утрачена')
                data = self.vk('groups.getLongPollServer', group_id = self.group_id)
                self.key = data['key']
                self.ts = data['ts']
            return []
        else:
            self.ts = data['ts']
            updates = []
            for update in data['updates']:
                updates.append(Update(update, self.vk))
            return updates

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

    def reply_to_peer(self, message, **kwargs):
        return self.vk.msg_op(1, self.message.peer_id, message, **kwargs)
        