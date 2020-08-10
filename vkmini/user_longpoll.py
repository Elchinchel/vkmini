from .request import longpoll_get
from .exceptions import TokenInvalid
from . import VkApi
from datetime import datetime

# from wtflog import warden
# logger = warden.get_boy('VK Group LongPoll')
from .printer import Printer
logger = Printer()


class LP:
    key: str
    server:str
    ts: int
    receive_time: float
    vk: VkApi
    wait: int

    def __init__(self, vk: VkApi, wait: int):
        self.vk = vk
        self.wait = wait

    @property
    async def check(self):
        data = await longpoll_get(f"http://{self.server}?act=a_check&key={self.key}&ts={self.ts}&wait={self.wait}&mode=2&version=10")

        self.receive_time = datetime.now().timestamp()

        if 'failed' in data.keys():
            if data['failed'] == 1:
                logger.error('Ошибка истории событий')
                self.ts = data['ts']
            elif data['failed'] == 2:
                self.key = await self.vk('messages.getLongPollServer')['key']
            else:
                raise Exception('Информация о пользователе утрачена')
            return []
        else:
            self.ts = data['ts']
            return data['updates']


async def create_user_poller(vk: VkApi, wait: int = 25) -> LP: # потому что руки из жопы, да
    lp = LP(vk, wait)
    data = await vk('messages.getLongPollServer')
    if data.get('error'):
        if data['error']['error_code'] == 5:
            raise TokenInvalid
    lp.server = data['server']
    lp.key = data['key']
    lp.ts = data['ts']
    return lp