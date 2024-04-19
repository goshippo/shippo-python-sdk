import shippo
import httpretty
from shippo.models.components import CarriersEnum
from tests.helpers_custom import get_carrier_account


BASE_URL = "http://localhost:9500"


class TestExperiment:

    @httpretty.activate(allow_net_connect=False)
    def test_signing(self):
        account_id = "12345"
        httpretty.register_uri(
            httpretty.GET,
            f"{BASE_URL}/carrier_accounts/{account_id}/signin/initiate",
            status=422,
            content_type="application/json",
            body='{"detail": "error"}'
        )

        sdk = shippo.Shippo(api_key_header="", server_url=BASE_URL)
        sdk.carrier_accounts.initiate_oauth2_signin(account_id, "")
