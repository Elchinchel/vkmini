import time

from typing import Any, Protocol, Deque
from asyncio import Future, get_running_loop
from functools import total_ordering
from collections import deque


class AbstractLogger(Protocol):
    def debug(self, __msg: str):
        raise NotImplementedError

    def warning(self, __msg: str):
        raise NotImplementedError


class Printer:
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

    def __init__(self):
        self._allowed = True
        self._waiters = deque()

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
            fut = get_running_loop().create_future()
            self._waiters.append(fut)
            await fut


@total_ordering
class Version:
    major: int
    minor: int

    def __init__(self, v: str) -> None:
        major, _, minor = v.partition('.')
        try:
            self.major, self.minor = int(major), int(minor)
        except ValueError:
            raise ValueError('Unsupported version format') from None

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Version):
            return NotImplemented
        return self.major == __o.major and self.minor == __o.minor

    def __lt__(self, __o: object) -> bool:
        if not isinstance(__o, Version):
            return NotImplemented
        return self.major <= __o.major and self.minor < __o.minor
