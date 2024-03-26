from typing import List

from shippo.models.components import Carriers, CarrierAccount
from shippo.models.operations import ListCarrierAccountsRequest

import shippo


def get_carrier_account(api: shippo.Shippo, carrier: Carriers) -> CarrierAccount:
    return get_carrier_accounts(api, carrier)[0]


def get_carrier_accounts(api: shippo.Shippo, carrier: Carriers) -> List[CarrierAccount]:
    carrier_accounts = api.carrier_accounts.list_carrier_accounts(request=ListCarrierAccountsRequest(
        carrier=carrier
    ))
    return carrier_accounts.carrier_account_list_wrapper.results
