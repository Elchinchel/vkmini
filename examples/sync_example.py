# TODO: синхронного LP-то нет))0)
from vkmini import VkApi

# создание экземпляра класса для работы с VK API в синхронном режиме
vk = VkApi(
    access_token='токен',
    sync_mode=True,
    excepts=True
)

# user = vk.users.get()[0]  # получение информации о текущем пользователе

# print(user)

# user_id = user['id']

# отправка сообщения в лс пользователю-владельцу токена (самому себе)
message_id = vk.messages.send(
    peer_id=0,
    message='Привет, мир!',
    random_id=0
)

print(message_id)
