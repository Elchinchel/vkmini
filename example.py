import asyncio
from vkmini import VkApi, LP, logger
from datetime import datetime

token = '<VK token>'
me_token = '<VK Me token>'

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

    elif text_lowered == 'скрин':

        # отправка execute запроса
        await vk.exe(
            '''return API.messages.sendService({
            peer_id:%s,
            action_type:"chat_screenshot",
            random_id:0
            });''' % update[3], me_token)

        # редактирование сообщения с последующим его удалением через 3 секунды
        # компактный вид:
        # vk.msg_op(2, update[3], 'Запрос отправлен!', update[1], 3)
        await vk.msg_op(
            mode = 2,
            peer_id = update[3],
            text = 'Запрос отправлен!',
            msg_id = update[1],
            delete_delay = 3
            )

async def main():
    vk = VkApi(token, logger=logger.Printer())
    lp = await LP.create_poller(vk)
    async for update in lp.listen(): # "прослушка" событий пользовательского longpoll
        if update[0] == 4 and update[2] & 2 == 2:
            await handle(update, vk, lp)

asyncio.run(main())
