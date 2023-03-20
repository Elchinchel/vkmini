from typing import Callable, Awaitable, Optional, Any, List, TYPE_CHECKING


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
    def _get(vk, name: str) -> Optional['MethodGroup']:
        if name in _API_METHOD_GROUPS:
            return MethodGroup(name, vk)
        return None

    @classmethod
    def _get_all(cls, vk) -> List['MethodGroup']:
        return [cls(name, vk) for name in _API_METHOD_GROUPS]

    def __init__(self, name, vk) -> None:
        self.name = name
        self.vk = vk

    def __getattr__(self, method: str) -> Callable[..., Awaitable[Any]]:
        def method_call(**kwargs):
            return self.vk(f'{self.name}.{method}', **kwargs)
        return method_call
