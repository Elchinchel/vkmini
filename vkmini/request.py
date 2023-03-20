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


async def _get_session(session: Optional[ClientSession]) -> Tuple[ClientSession, bool]:
    if not (default_session or session):
        return ClientSession(), True
    return (session or default_session), False  # type: ignore


def check_longpoll_session(session: Optional[ClientSession]):
    if not (session or default_session):
        warn(ResourceWarning(
            'При создании экземпляра LP не была указана сессия, при этом '
            'сессия default_session также не задана. Это приведёт к '
            'созданию новой сессии на каждый запрос.'
        ))


async def _make_request(client_session, caller, **caller_kwargs):
    session, should_close = await _get_session(client_session)
    try:
        async with caller(session, **caller_kwargs) as resp:
            if resp.status == 200:
                return await resp.json(loads=json_decoder)
            else:
                raise NetworkError(resp.status)
    finally:
        if should_close:
            await session.close()


async def post(
        url: str,
        data: dict,
        client_session: Optional[ClientSession] = None
) -> dict:
    return await _make_request(
        client_session, ClientSession.post, url=url, data=data
    )


async def get(
        url: str,
        client_session: Optional[ClientSession] = None
) -> dict:
    return await _make_request(
        client_session, ClientSession.get, url=url
    )
