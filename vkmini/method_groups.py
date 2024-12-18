from typing import Any, List, Callable, Optional, Awaitable


_API_METHOD_GROUPS = (
    'account',
    'ads',
    'adsweb',
    'apps',
    'appWidgets',
    'asr',
    'auth',
    'board',
    'bugtracker',
    'calls',
    'database',
    'docs',
    'donut',
    'downloadedGames',
    'fave',
    'friends',
    'gifts',
    'groups',
    'leadForms',
    'likes',
    'market',
    'messages',
    'newsfeed',
    'notes',
    'notifications',
    'orders',
    'pages',
    'photos',
    'podcasts',
    'polls',
    'prettyCards',
    'search',
    'secure',
    'stats',
    'status',
    'storage',
    'store',
    'stories',
    'streaming',
    'translations',
    'users',
    'utils',
    'video',
    'wall',
    'widgets',
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
