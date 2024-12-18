from typing import Optional

from aiohttp import ClientSession, ClientResponse

from vkmini.exceptions import NetworkError


async def _make_request(client_session: Optional[ClientSession], caller, **caller_kwargs):
    should_close = (client_session is None)
    session = client_session or ClientSession()
    try:
        async with caller(session, **caller_kwargs) as resp:
            resp: ClientResponse

            if resp.status == 200:
                return await resp.json()
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
