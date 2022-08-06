# VKmini

Лёгкая библиотека, "оборачивающая" запросы к API vk.com

Параметры запросов и ответы библиотекой не модифицируются,
поведение методов максимально соответствует официальной [документации API](https://vk.com/dev/methods)

## Установка

```
pip install vkmini
```

## Пример использования:

```python
import asyncio
import vkmini

vk = vkmini.VkApi(access_token='токен', excepts=True)

async def main():
    print(await vk.users.get())

asyncio.run(main())
```

Больше примеров [здесь](https://github.com/Elchinchel/vkmini/tree/master/examples)