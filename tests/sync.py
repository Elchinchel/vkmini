from vkmini import VkApi

vk = VkApi('')

vk.switch_to_sync()

print(vk.users.get())

vk.switch_to_async()

print(vk.users.get())
