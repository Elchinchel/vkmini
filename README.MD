# VKmini

Махонькая библиотека для почти прямой работы с VK API

## Установка

```
pip install vkmini
```

## Примеры использования:

### Синхронный режим
```python
from vkmini import VkApi

vk = VkApi(access_token='токен', sync_mode=True, excepts=True)

print(vk.users.get())
```
### Асинхронный режим
```python
import asyncio
import vkmini

vk = vkmini.VkApi(access_token='токен', excepts=True)

async def main():
    print(await vk.users.get())

asyncio.get_event_loop().run_until_complete(main())
```

Больше примеров в [тута](https://github.com/Elchinchel/vkmini/tree/master/examples)