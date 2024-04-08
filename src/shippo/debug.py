from contextvars import ContextVar
from typing import Optional

from requests import Session, PreparedRequest, Response


class DebugSession(Session):

    _last_request: ContextVar
    _last_response: ContextVar

    def __init__(self):
        super().__init__()
        self._last_request = ContextVar("last_request", default=None)
        self._last_response = ContextVar("last_response", default=None)

    def clear(self):
        self._last_request.set(None)
        self._last_response.set(None)

    @property
    def last_request(self) -> Optional[PreparedRequest]:
        return self._last_request.get()

    @property
    def last_response(self) -> Optional[Response]:
        return self._last_response.get()

    def send(self, request, **kwargs):
        self._last_request.set(request)
        self._last_response.set(None)
        response = Session.send(self, request, **kwargs)
        self._last_response.set(response)
        return response
