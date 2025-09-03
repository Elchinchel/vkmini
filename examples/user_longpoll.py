import asyncio
import logging

from vkmini import VkApi, UserLP


API_ACCESS_TOKEN = 'Ключ доступа к API'

logging.basicConfig(level=logging.DEBUG)

vk = VkApi(
    access_token=API_ACCESS_TOKEN,  # Ключ доступа к API
    version='5.199',  # Версия API, по умолчанию совпадает с версией библиотеки
)


async def main():
    async with UserLP(vk) as lp:
        # контекст-менеджер используется для создания новой сессии и её закрытия

        async for event in lp.listen():  # lp.listen() создаёт асинхронный генератор событий,
            print(event)           # события возвращаются в том же формате, в котором приходят от VK

            event_type = event[0]  # код события, про все коды можно почитать в документации:
                                   #     https://vk.ru/dev/using_longpoll_2?f=3.%2BСтруктура%2Bсобытий

            if event_type != 4:  # событие 4 -- новое сообщение. Если это не оно, пропускаем.
                continue

            message_flags = event[2]  # флаги полученного сообщения. Подробнее:
                                      #     https://vk.ru/dev/using_longpoll_3?f=4.%20Флаги%20сообщений

            if message_flags & 2 != 2:  # пропускаем входящие сообщения
                continue

            message_text = event[5]  # текст полученного сообщения

            if message_text.lower() == 'пинг':
                # отправка нового сообщения в чат, из которого пришло событие,
                # используется метод messages.send: https://vk.ru/dev/messages.send
                await vk.messages.send(
                    peer_id=event[3],
                    message='Понг!',
                    random_id=0
                )


asyncio.run(main())
