import time

def _print(text):
    print(time.localtime(), text)

class Printer:
    level: int = 1

    def critical(self, text):
        print(text)

    def error(self, text):
        if self.level < 5: print(text)

    def warning(self, text):
        if self.level < 4: print(text)

    def info(self, text):
        if self.level < 3: print(text)

    def debug(self, text):
        if self.level < 2: print(text)