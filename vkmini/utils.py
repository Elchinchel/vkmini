import time

from abc import ABC, abstractmethod
from typing import Any, Callable, Deque
from asyncio import Future
from collections import deque


class AbstractLogger(ABC):
    @abstractmethod
    def debug(self, msg: str):
        raise NotImplementedError

    @abstractmethod
    def info(self, msg: str):
        raise NotImplementedError

    @abstractmethod
    def warning(self, msg: str):
        raise NotImplementedError

    @abstractmethod
    def error(self, msg: str):
        raise NotImplementedError


class Printer(AbstractLogger):
    """
    Реализует распространённый интерфейс логгера,
    выводит логируемые сообщения в sys.stdout
    """
    level: int

    def __init__(self, level: int = 2) -> None:
        self.level = level

    @staticmethod
    def __print(level_name, msg):
        print(
            time.strftime('%H:%M:%S', time.localtime()),
            level_name,
            msg
        )

    def critical(self, msg: Any):
        self.__print('CRITICAL', msg)

    def error(self, msg: Any):
        if self.level < 5:
            self.__print('ERROR', msg)

    def warning(self, msg: Any):
        if self.level < 4:
            self.__print('WARNING', msg)

    def info(self, msg: Any):
        if self.level < 3:
            self.__print('INFO', msg)

    def debug(self, msg: Any):
        if self.level < 2:
            self.__print('DEBUG', msg)


class Blocker:
    _waiters: Deque[Future]

    def __init__(self, future_factory: Callable[[], Future]):
        self._allowed = True
        self._waiters = deque()
        self._create_future = future_factory

    def is_allowed(self) -> bool:
        return self._allowed

    def release_one(self):
        while self._waiters:
            waiter = self._waiters.popleft()
            if not waiter.done():
                waiter.set_result(True)
                break
        if not self._waiters:
            self._allowed = True

    def block(self):
        self._allowed = False

    async def wait(self):
        if not self._allowed:
            fut = self._create_future()
            self._waiters.append(fut)
            await fut
