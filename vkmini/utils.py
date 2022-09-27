import time

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
    """
    Реализует распространённый интерфейс логгера,
    выводит логируемые сообщения в sys.stdout
    """
    level: int = 1

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
