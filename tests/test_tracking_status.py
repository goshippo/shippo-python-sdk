import httpretty
import pytest

import shippo

BASE_URL = "http://localhost:9500"
TRACK_BODY = (
    '{"carrier": "usps", "tracking_number": "9205590164917312751089", '
    '"messages": [], "tracking_history": []}'
)


def make_sdk():
    return shippo.Shippo(api_key_header="shippo_test_12345", server_url=BASE_URL)


class TestTrackingStatusGet:
    """tracking_status.get must not accept positional arguments.

    The URL is /tracks/{carrier}/{tracking_number}, but the generated signature lists
    tracking_number first. In 3.x a positional call in URL order swapped the two values.
    """

    def test_positional_call_raises(self):
        with pytest.raises(TypeError):
            make_sdk().tracking_status.get("usps", "9205590164917312751089")

    @pytest.mark.asyncio
    async def test_positional_call_raises_async(self):
        with pytest.raises(TypeError):
            await make_sdk().tracking_status.get_async("usps", "9205590164917312751089")

    @httpretty.activate(allow_net_connect=False)
    def test_keyword_call_builds_carrier_first_path(self):
        httpretty.register_uri(
            httpretty.GET,
            f"{BASE_URL}/tracks/usps/9205590164917312751089",
            content_type="application/json",
            body=TRACK_BODY,
        )

        make_sdk().tracking_status.get(tracking_number="9205590164917312751089", carrier="usps")

        assert httpretty.last_request().path == "/tracks/usps/9205590164917312751089"
