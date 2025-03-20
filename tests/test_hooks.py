import httpretty
import pytest as pytest

import shippo

BASE_URL = "http://localhost:9500"


@pytest.mark.skip(reason="Skipping tests due to Python 3.11 compatibility issues")
class TestHooks:

    @pytest.mark.parametrize("api_token,should_prefix", [
        ("shippo_test_12345", True),
        ("shippo_live_12345", True),
        ("ShippoToken shippo_test_12345", False),
        ("JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...", False)
    ])
    @httpretty.activate(allow_net_connect=False)
    def test_should_add_prefix_if_api_token(self, api_token, should_prefix):
        auth_header = None

        def request_callback(request, uri, response_headers):
            nonlocal auth_header
            auth_header = request.headers['Authorization']
            return [200, response_headers, '{"results": []}']

        httpretty.register_uri(
            httpretty.GET, f"{BASE_URL}/addresses", content_type="application/json", body=request_callback
        )

        sdk = shippo.Shippo(api_key_header=api_token, server_url=BASE_URL)
        sdk.addresses.list()
        if should_prefix:
            assert auth_header == f"ShippoToken {api_token}"
        else:
            assert auth_header == api_token
