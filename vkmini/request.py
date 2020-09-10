from .exceptions import NetworkError
from aiohttp import ClientSession


async def post(url: str, data: dict, excepts: bool = False) -> dict:
    async with ClientSession() as session:
        async with session.post(url, data=data) as resp:
            if resp.status == 200:
                return await resp.json()
            elif excepts:
                raise NetworkError(resp.status)


async def longpoll_get(url: str, excepts: bool = False) -> dict:
    async with ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                return await resp.json()
            else:
                if excepts:
                    raise NetworkError(resp.status)
                return {}
