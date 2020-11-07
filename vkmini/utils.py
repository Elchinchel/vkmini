import time
from abc import ABC, abstractmethod


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
