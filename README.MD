# VKmini

запрашивалка вконтакта с тайпхинтами
(параметры запросов и ответы никак не модифицируются библиотекой)

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
