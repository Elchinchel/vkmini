import asyncio
from vkmini import VkApi, LP

token = 'токен'

vk = VkApi(token, True)


async def handle_outgoing_message(update: list) -> None:
    if update[5].lower() == 'пинг':
        # отправка нового сообщения в чат, из которого пришло событие
        await vk.messages.send(
            peer_id=update[3],
            message='Понг!',
            random_id=0
        )


async def main():
    async with LP(vk) as lp:
        # контекст-менеджер используется для создания новой сессии и её закрытия
        async for update in lp.listen():  # "прослушка" событий user longpoll
            print(update)
            if update[0] == 4 and update[2] & 2 == 2:
                await handle_outgoing_message(update)


asyncio.run(main())
