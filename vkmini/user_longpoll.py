import time
from typing import Generator, List, Any

from .utils import AbstractLogger
from .request import longpoll_get
from .exceptions import TokenInvalid
from . import VkApi


class LP:
    key: str
    server: str
    ts: int
    receive_time: float
    vk: VkApi
    wait: int

    def __init__(self, vk: VkApi, wait: int):
        'Для создания экземпляра используйте метод `new`'
        self.vk = vk
        self.wait = wait

    @staticmethod
    async def new(vk: VkApi, wait: int = 25,
                  logger: AbstractLogger = None) -> "LP":
        lp = LP(vk, wait)
        lp.logger = logger or vk.logger
        data = await vk('messages.getLongPollServer')
        if data.get('error'):
            if data['error']['error_code'] == 5:
                raise TokenInvalid(data['error'])
        lp.server = data['server']
        lp.key = data['key']
        lp.ts = data['ts']
        return lp

    @property
    async def check(self) -> List[List[Any]]:
        data = await longpoll_get(
            f"http://{self.server}?act=a_check&key={self.key}&ts={self.ts}&wait={self.wait}&mode=2&version=10",
            self.vk.excepts
            )

        self.receive_time = time.time()

        if 'failed' in data.keys():
            if data['failed'] == 1:
                if self.logger:
                    self.logger.error('Ошибка истории событий')
                self.ts = data['ts']
            elif data['failed'] == 2:
                self.key = (await self.vk('messages.getLongPollServer'))['key']
            else:
                if self.logger:
                    self.logger.error('Информация о пользователе утрачена')
                if self.vk.excepts:
                    # TODO: придумать что нибудь другое сюда
                    raise Exception('Информация о пользователе утрачена')
            return []
        else:
            self.ts = data['ts']
            return data['updates']

    async def listen(self) -> Generator[list, None, None]:
        while True:
            for update in await self.check:
                yield update
