from typing import Deque
from asyncio import Future, get_running_loop
from collections import deque


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


def parse_api_version(version: str):
    parts = version.split('.')
    assert len(parts) == 2
    return tuple(map(int, parts))
