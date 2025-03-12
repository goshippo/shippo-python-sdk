import pytest
from marshmallow import ValidationError

import shippo
from shippo.models.components import CarriersEnum, ConnectExistingOwnAccountRequest
from shippo.models.operations import ListCarrierAccountsRequest


class TestCarrierAccounts:

    def test_list_all_carrier_accounts(self, api: shippo.Shippo):
        for carrier in CarriersEnum:
            request = ListCarrierAccountsRequest(carrier=carrier)
            carrier_accounts = api.carrier_accounts.list(request=request)

            assert carrier_accounts is not None
            assert carrier_accounts.results is not None

            if len(carrier_accounts.results) > 0:
                for carrier_account in carrier_accounts.results:
                    assert carrier_account.carrier == carrier
                    assert carrier_account.object_id is not None
                    assert carrier_account.object_owner is not None
                    assert carrier_account.test is not None

    def test_parameters_deserialize_to_dict(self, api: shippo.Shippo):
        parameters = {
            "api_version": 4,
            "username": "12345",
            "password": "password",
            "pickup_no": "12345",
            "facility_code": "1234",
        }

        request_data = {
            "account_id": "123456789",
            "carrier": "dhl_ecommerce",
            "parameters": parameters,
            "metadata": "DHLEcomTestAccount",
            "active": False,
            "test": False,
        }

        try:

            request = ConnectExistingOwnAccountRequest.model_validate(request_data)
            assert isinstance(request.parameters, dict)
            for key, value in request.parameters.items():
                assert key in parameters
                assert value is not None

        except ValidationError as e:
            pytest.fail(f"Deserialization failed with ValidationError: {e}")
        except Exception as e:
            pytest.fail(f"Unexpected error occurred: {e}")
