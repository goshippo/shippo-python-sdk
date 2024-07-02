import json
import os

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
        # NOTE: this requires a valid API token.  I just add `SHIPPO_TOKEN=<personal test token>` to the Python
        # test template configuration (Autodetect) in IntelliJ, so it gets picked up whenever a test is run.
        # alternatively, you can just replace `os.environ...` with your actual API token, just don't check it in.
        token = os.environ['SHIPPO_TOKEN']
        return shippo.Shippo(client=debug_session, api_key_header=token)

    def test_experiment(self, debug_session: DebugSession, debug_api: shippo.Shippo):
        debug_api.addresses.list()
        last_response = debug_session.last_response.json()
        # sometimes, you'll want to inspect the raw json coming back from the server, in cases where the
        # API spec isn't complete or the model is slightly off.
        print(json.dumps(last_response, indent=2))

