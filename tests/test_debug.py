import asyncio
from concurrent.futures import ThreadPoolExecutor
from random import randint

import httpretty as httpretty
import pytest

import shippo
from shippo.debug import DebugSession

BASE_URL = "http://localhost:9500"


class TestDebugClient:

    @pytest.fixture(scope='session')
    def debug_session(self):
        return DebugSession()

    @pytest.fixture(scope='session')
    def debug_api(self, debug_session: DebugSession):
        return shippo.Shippo(client=debug_session, api_key_header="", server_url=BASE_URL)

    @staticmethod
    def invoke_api_and_verify_request_and_response_are_set(
            debug_session: DebugSession, debug_api: shippo.Shippo
    ):
        page = randint(1, 100)
        debug_api.addresses.list(page=page)
        assert debug_session.last_request is not None
        assert str(debug_session.last_request.url).endswith(f"?page={page}")
        assert debug_session.last_response is not None

    @httpretty.activate(allow_net_connect=False)
    def test_should_record_request_and_response(
            self, debug_session: DebugSession, debug_api: shippo.Shippo
    ):
        httpretty.register_uri(
            httpretty.GET, f"{BASE_URL}/addresses", content_type="application/json", body='{"results": []}'
        )

        self.invoke_api_and_verify_request_and_response_are_set(debug_session, debug_api)

    @httpretty.activate(allow_net_connect=False)
    def test_should_record_request_and_response_across_threads(
            self, debug_session: DebugSession, debug_api: shippo.Shippo
    ):
        httpretty.register_uri(
            httpretty.GET, f"{BASE_URL}/addresses", content_type="application/json", body='{"results": []}'
        )

        debug_session.clear()
        
        with ThreadPoolExecutor(max_workers=1) as executor:
            future1 = executor.submit(self.invoke_api_and_verify_request_and_response_are_set, debug_session, debug_api)
            future2 = executor.submit(self.invoke_api_and_verify_request_and_response_are_set, debug_session, debug_api)

            future1.result()
            future2.result()

        assert debug_session.last_request is None
        assert debug_session.last_response is None

    @staticmethod
    async def async_invoke_api_and_verify_request_and_response_are_set(
            debug_session: DebugSession, debug_api: shippo.Shippo
    ):
        page = randint(1, 100)
        debug_api.addresses.list(page=page)
        assert debug_session.last_request is not None
        assert str(debug_session.last_request.url).endswith(f"?page={page}")
        assert debug_session.last_response is not None

    @httpretty.activate(allow_net_connect=False)
    def test_should_record_request_and_response_across_async_tasks(
            self, debug_session: DebugSession, debug_api: shippo.Shippo
    ):
        httpretty.register_uri(
            httpretty.GET, f"{BASE_URL}/addresses", content_type="application/json", body='{"results": []}'
        )

        debug_session.clear()

        async def run_async():
            await asyncio.gather(
                self.async_invoke_api_and_verify_request_and_response_are_set(debug_session, debug_api),
                self.async_invoke_api_and_verify_request_and_response_are_set(debug_session, debug_api)
            )

        asyncio.run(run_async())

        assert debug_session.last_request is None
        assert debug_session.last_response is None
