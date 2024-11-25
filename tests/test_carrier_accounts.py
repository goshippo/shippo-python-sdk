import shippo
from shippo.models.components import CarriersEnum, ConnectExistingOwnAccountRequest
from shippo.models.operations import ListCarrierAccountsRequest


class TestCarrierAccounts:

    def test_list_all_carrier_accounts(self, api: shippo.Shippo):
        for carrier in CarriersEnum:
            request = ListCarrierAccountsRequest(carrier=carrier)
            carrier_accounts = api.carrier_accounts.list(request=request)

            assert carrier_accounts is not None

            if len(carrier_accounts.results) > 0:
                for carrier_account in carrier_accounts.results:
                    assert carrier_account.carrier == carrier
                    assert carrier_account.object_id is not None
                    assert carrier_account.object_owner is not None
                    assert carrier_account.test is not None
