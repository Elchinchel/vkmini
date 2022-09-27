from typing import Coroutine, List, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .api import VkApi


_API_METHOD_GROUPS = (
    'account',
    'ads',
    'apps',
    'audio',
    'board',
    'database',
    'docs',
    'fave',
    'friends',
    'gifts',
    'groups',
    'likes',
    'market',
    'messages',
    'newsfeed',
    'notes',
    'notifications',
    'pages',
    'photos',
    'places',
    'polls',
    'search',
    'secure',
    'store',
    'stats',
    'status',
    'storage',
    'users',
    'utils',
    'video',
    'podcasts',
    'leadforms',
    'prettycards',
    'stories',
    'appwidgets',
    'streaming',
    'orders',
    'wall',
    'widgets'
)


class MethodGroup:
    name: str

    @staticmethod
    def _get(vk: 'VkApi', name: str) -> Optional['MethodGroup']:
        if name in _API_METHOD_GROUPS:
            return MethodGroup(name, vk)
        return None

    @classmethod
    def _get_all(cls, vk: 'VkApi') -> List['MethodGroup']:
        return [cls(name, vk) for name in _API_METHOD_GROUPS.keys()]

    def __init__(self, name, vk) -> None:
        self.name = name
        self.vk = vk

    def __getattr__(self, method: str) -> Coroutine:
        def method_call(**kwargs):
            return self.vk(f'{self.name}.{method}', **kwargs)
        return method_call
