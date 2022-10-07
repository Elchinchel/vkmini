# TODO: жидковато
from vkmini import GroupVkApi, GroupLP
import asyncio


token: str = '<API токен VK группы>'
group_id: int = 0  # ID группы


async def main():
    vk = GroupVkApi(token, excepts=True)
    async with GroupLP(vk, group_id) as lp:
        async for update in lp.listen():
            print(update)


asyncio.run(main())
