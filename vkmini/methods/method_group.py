from typing import Callable, Coroutine, Union


class MethodGroup:
    name: str

    def __init__(self, name: str, vk) -> None:
        self.name = name
        self.vk = vk

    def __getattr__(self, method: str) -> Union[Coroutine, Callable]:
        if self.vk.sync:
            def method_call(**kwargs):
                return self.vk.sync_call(f'{self.name}.{method}', **kwargs)
        else:
            async def method_call(**kwargs):
                return await self.vk(f'{self.name}.{method}', **kwargs)
        return method_call

    @staticmethod
    def get_known_methods() -> dict:
        raise NotImplementedError
