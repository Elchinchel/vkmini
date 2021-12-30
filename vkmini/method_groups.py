from typing import Callable, Coroutine, Union


method_groups = {
    'account': '',
    'ads': '',
    'apps': '',
    'audio': '',
    'board': '',
    'database': '',
    'docs': '',
    'fave': '',
    'friends': '',
    'gifts': '',
    'groups': '',
    'likes': '',
    'market': '',
    'messages': 'Методы для работы с личными сообщениями',
    'newsfeed': '',
    'notes': '',
    'notifications': '',
    'pages': '',
    'photos': '',
    'places': 'Методы для работы с местами',
    'polls': '',
    'search': '',
    'secure': '',
    'stats': '',
    'status': '',
    'storage': '',
    'users': '',
    'utils': '',
    'video': '',
    'podcasts': '',
    'leadforms': '',
    'prettycards': '',
    'stories': '',
    'appwidgets': '',
    'streaming': '',
    'orders': '',
    'wall': '',
    'widgets': ''
}


class MethodGroup:
    name: str

    def __init__(self, name: str, vk) -> None:
        self.name = name
        self.vk = vk

    def __getattr__(self, method: str) -> Union[Coroutine, Callable]:
        if self.vk.sync:
            def method_call(**kwargs):
                return self.vk(f'{self.name}.{method}', **kwargs)
        else:
            async def method_call(**kwargs):
                return await self.vk(f'{self.name}.{method}', **kwargs)
        return method_call
