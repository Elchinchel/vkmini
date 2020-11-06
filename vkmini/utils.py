from queue import Queue
from abc import ABC, abstractmethod


class LoggerType(ABC):
    @abstractmethod
    def debug(self, text: str):
        raise NotImplementedError

    @abstractmethod
    def info(self, text: str):
        raise NotImplementedError

    @abstractmethod
    def error(self, text: str):
        raise NotImplementedError


async def sync_wrapper(queue: Queue, coro):
    try:
        queue.put((await coro, None))
    except Exception as e:
        queue.put((None, e))
