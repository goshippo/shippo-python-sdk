from contextvars import ContextVar
from typing import Optional, Union
import httpx


class DebugSession(httpx.Client):
    _last_request: ContextVar
    _last_response: ContextVar

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._last_request = ContextVar("last_request", default=None)
        self._last_response = ContextVar("last_response", default=None)

    def clear(self):
        self._last_request.set(None)
        self._last_response.set(None)

    @property
    def last_request(self) -> Optional[httpx.Request]:
        return self._last_request.get()

    @property
    def last_response(self) -> Optional[httpx.Response]:
        return self._last_response.get()

    def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        self._last_request.set(request)
        self._last_response.set(None)
        response = super().send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )
        self._last_response.set(response)
        return response
