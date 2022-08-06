from typing import Coroutine, List, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .api import VkApi


_method_groups = {
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

    @staticmethod
    def _get(vk: 'VkApi', name: str) -> Optional['MethodGroup']:
        if name in _method_groups:
            return MethodGroup(name, vk)
        return None

    @staticmethod
    def _get_all(vk: 'VkApi') -> List['MethodGroup']:
        return [MethodGroup(name, vk) for name in _method_groups.keys()]

    def __init__(self, name, vk) -> None:
        self.name = name
        self.vk = vk

    def __getattr__(self, method: str) -> Coroutine:
        async def method_call(**kwargs):
            return await self.vk(f'{self.name}.{method}', **kwargs)
        return method_call
