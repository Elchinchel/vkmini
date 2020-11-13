from vkmini import VkApi

# создание экземпляра класса для работы с VK API в синхронном режиме
vk = VkApi(
    access_token='токен',
    sync_mode=True,
    excepts=True
)

user = vk.users.get()[0]  # получение информации о текущем пользователе

print(user)
# user - информация, возвращаемая методом users.get в поле "response"
# подробнее -- https://vk.com/dev/users.get

user_id = user['id']

# отправка сообщения в лс пользователю-владельцу токена (самому себе)
message_id = vk.messages.send(
    peer_id=0,
    message='Привет, мир!',
    random_id=0
)

print(message_id)
# message_id - информация, возвращаемая методом messages.send в поле "response"
# подробнее -- https://vk.com/dev/messages.send
