import time
import asyncio

from abc import ABC, abstractmethod
from typing import Any


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
    '''
    Реализует стандартный интерфейс логгера, выводит текст в sys.stdout
    '''
    level: int = 1

    def __init__(self, level: int = 2) -> None:
        self.level = level

    @staticmethod
    def __print(msg):
        print(time.strftime('%H:%M:%S', time.localtime()), msg)

    def critical(self, msg):
        self.__print(msg)

    def error(self, msg):
        if self.level < 5:
            self.__print(msg)

    def warning(self, msg):
        if self.level < 4:
            self.__print(msg)

    def info(self, msg):
        if self.level < 3:
            self.__print(msg)

    def debug(self, msg):
        if self.level < 2:
            self.__print(msg)
