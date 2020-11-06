# TODO: синхронного LP-то нет))0)
from vkmini import VkApi

vk = VkApi(
    access_token='токен',
    sync_mode=True,
    excepts=True
)

print(vk.users.get())
