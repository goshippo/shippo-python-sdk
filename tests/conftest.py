import os

import pytest
from shippo.models.components import AddressCreateRequest

import shippo


@pytest.fixture(scope='session')
def api():
    token = os.environ['SHIPPO_TOKEN']
    return shippo.Shippo(
        api_key_header=token
    )


@pytest.fixture(scope='session')
def create_address_request() -> AddressCreateRequest:
    """Fixture to create a reusable address."""
    return AddressCreateRequest(
        country='US',
        name='Shwan Ippotle',
        company='Shippo',
        street1='215 Clayton St.',
        street3='',
        street_no='',
        city='San Francisco',
        state='CA',
        zip='94117',
        phone='+1 555 341 9393',
        email='shippotle@shippo.com',
        is_residential=True,
        metadata='Customer ID 123456',
        validate=True,
    )
