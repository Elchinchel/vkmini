import json

from typing import Optional, Tuple, Union
from aiohttp import ClientSession
from warnings import warn

from vkmini.exceptions import NetworkError


default_session: Union[ClientSession, None] = None
json_decoder = json.loads


def set_decoder(loads) -> None:
    """
    Устанавливает функцию, которая будет использоваться при
    десериализации ответа на запросы
    """
    global json_decoder
    json_decoder = loads


def set_session(session: ClientSession) -> None:
    """
    Устанавливает сессию, которая будет использоваться по умолчанию при
    любых запросах к API, в т.ч. LongPoll (исключение - обращение к API c
    помощью обектов, при создании которых была явно передана сессия)

    Разумеется, стоит позаботиться о закрытии этой сессии перед завершением
    работы приложения

    Если при запросе не указана сессия (не установлена стандартная или не
    передана в конструктор при создании класса), на каждый новый запрос
    будет создаваться новая сессия (это плохое решение, лучше создать и
    указать сессию)
    """
    global default_session
    default_session = session


async def _get_session(session) -> Tuple[ClientSession, bool]:
    if not (default_session or session):
        return ClientSession(), True
    return (session or default_session), False


def _check_longpoll_session(session: Optional[ClientSession]):
    if not (session or default_session):
        warn(ResourceWarning(
            'При создании экземпляра LP не была указана сессия, при этом '
            'сессия default_session также не задана. Это приведёт к '
            'созданию новой сессии на каждый запрос.'
        ))


async def post(url: str,
               data: dict,
               client_session: ClientSession = None) -> dict:
    session, should_close = await _get_session(client_session)
    async with session.post(url, data=data) as resp:
        if resp.status == 200:
            data = await resp.json(loads=json_decoder)
        else:
            data = {}
    if should_close:
        await session.close()
    if data:
        return data
    raise NetworkError(resp.status)


async def longpoll_get(url: str,
                       client_session: ClientSession = None) -> dict:
    session, should_close = await _get_session(client_session)
    async with session.get(url) as resp:
        if resp.status == 200:
            data = await resp.json(loads=json_decoder)
        else:
            data = {}
    if should_close:
        await session.close()
    if data:
        return data
    raise NetworkError(resp.status)


async def get(url: str, client_session: ClientSession = None) -> bytes:
    session, should_close = await _get_session(client_session)
    try:
        async with session.get(url) as resp:
            if resp.status == 200:
                return await resp.content.read()
            else:
                raise NetworkError(resp.status)
    finally:
        if should_close:
            await session.close()
