import time
import asyncio
from abc import ABC, abstractmethod
from typing import Any, Union


def run_coro_sync(coro, loop: asyncio.AbstractEventLoop) -> Any:
    if loop.is_running():
        return asyncio.run_coroutine_threadsafe(coro, loop).result()
    else:
        return loop.run_until_complete(coro)


class AbstractCaptchaSolver(ABC):
    @abstractmethod
    async def solve(image_link: str) -> Union[str, None]:
        raise NotImplementedError

    async def callback(VkApi, method: str, data: dict) -> Any:
        pass


class AbstractLogger(ABC):
    @abstractmethod
    def debug(self, text: str):
        raise NotImplementedError

    @abstractmethod
    def info(self, text: str):
        raise NotImplementedError

    @abstractmethod
    def error(self, text: str):
        raise NotImplementedError


class Printer(AbstractLogger):
    level: int = 1

    def __init__(self, level: int = 2) -> None:
        self.level = level

    def __print(text):
        print(time.strftime('%H:%M:%S', time.localtime()), text)

    def critical(self, text):
        self.__print(text)

    def error(self, text):
        if self.level < 5:
            self.__print(text)

    def warning(self, text):
        if self.level < 4:
            self.__print(text)

    def info(self, text):
        if self.level < 3:
            self.__print(text)

    def debug(self, text):
        if self.level < 2:
            self.__print(text)
