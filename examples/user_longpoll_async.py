# TODO: не работает с последней версией либы
import asyncio
from vkmini import VkApi, LP

token = '<VK token>'

vk = VkApi(token, True)

async def handle(update: list, vk: VkApi, lp: LP):
    text_lowered = update[5].lower()
    if text_lowered == 'тест':

        # отправка нового сообщения
        await vk.msg_op(
            mode = 1,
            peer_id = update[3],
            text = f'''Хэй!\nСообщение получено через {
            round(lp.receive_time - update[4], 1)
            }с. (±0.5)'''
            )


async def main():
    vk = VkApi(token, logger=logger.Printer())
    lp = await LP.new(vk)
    async for update in lp.listen(): # "прослушка" событий пользовательского longpoll
        if update[0] == 4 and update[2] & 2 == 2:
            await handle(update, vk, lp)

asyncio.run(main())
