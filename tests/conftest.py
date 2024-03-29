import os

import pytest

import shippo


@pytest.fixture(scope='session')
def api():
    token = os.environ['SHIPPO_TOKEN']
    return shippo.Shippo(
        api_key_header=token
    )
