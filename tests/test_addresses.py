import json

from helpers_custom import get_first_address_object_id
from shippo.models import components

from shippo.models.components import AddressPaginatedList, Address

import shippo


class TestAddresses:

    def test_get_address_list_success(self, api: shippo.Shippo):
        response = api.addresses.list()

        assert isinstance(response, AddressPaginatedList)
        assert len(response.results) >= 1
        assert response is not None
        print(response)

    def test_create_address_success(self, api: shippo.Shippo, create_address_request):
        response = api.addresses.create(request=create_address_request)

        assert response is not None
        assert response.object_id is not None
        assert isinstance(response, Address)
        assert response is not None
        assert response.object_id is not None
        assert isinstance(response, Address)
        assert response.validation_results.is_valid is True
        assert response.country == 'US'
        assert response.name == 'Shwan Ippotle'
        assert response.company == 'Shippo'
        assert response.street1 == '215 Clayton St'
        assert response.city == 'San Francisco'
        assert response.state == 'CA'
        assert response.zip == '94117-1913'
        assert response.email == 'shippotle@shippo.com'
        assert response.is_residential is True
        # This isn't being saved
        #assert response.metadata == 'Customer ID 123456'

    def test_get_address_success(self, api: shippo.Shippo):
        address_id = get_first_address_object_id(api)
        assert address_id is not None
        assert isinstance(address_id, str)

        response = api.addresses.get(address_id=address_id)

        assert response is not None
        assert response.object_id is not None
        assert isinstance(response, Address)
        assert response is not None
        assert response.object_id is not None
        assert isinstance(response, Address)
        assert response.validation_results.is_valid is True
        assert response.country == 'US'
        assert response.name == 'Shwan Ippotle'
        assert response.company == 'Shippo'
        assert response.street1 == '215 Clayton St'
        assert response.city == 'San Francisco'
        assert response.state == 'CA'
        assert response.zip == '94117-1913'
        assert response.email == 'shippotle@shippo.com'
        assert response.is_residential is True
        # This isn't being saved
        #assert response.metadata == 'Customer ID 123456'

    def test_validate_address_success(self, api: shippo.Shippo):
        address_id = get_first_address_object_id(api)
        assert address_id is not None
        assert isinstance(address_id, str)

        response = api.addresses.validate(address_id=address_id)

        assert response is not None
        assert response.object_id is not None
        assert isinstance(response, Address)
        assert response.validation_results.is_valid is True
        assert response.country == 'US'
        assert response.name == 'Shwan Ippotle'
        assert response.company == 'Shippo'
        assert response.street1 == '215 Clayton St'
        assert response.city == 'San Francisco'
        assert response.state == 'CA'
        assert response.zip == '94117-1913'
        assert response.email == 'shippotle@shippo.com'
        assert response.is_residential is True
        # This isn't being saved
        #assert response.metadata == 'Customer ID 123456'
