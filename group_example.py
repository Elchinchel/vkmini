from vkmini import VkApi, LPGroup
import asyncio

# chisto porzhatb

token: str = '<Токен VK группы>'
group_id: int = 0 # ID группы

async def main():
    vk = VkApi(token, excepts=True)
    lp = await LPGroup.create_poller(vk, group_id)
    async for update in lp.listen():
        if update.message.text.lower() == 'привет':
            await update.reply_to_peer('Привет!')

asyncio.run(main())