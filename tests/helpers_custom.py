from typing import List

from shippo.models.components import CarriersEnum, CarrierAccount
from shippo.models.operations import ListCarrierAccountsRequest

import shippo


def get_carrier_account(api: shippo.Shippo, carrier: CarriersEnum) -> CarrierAccount:
    return get_carrier_accounts(api, carrier)[0]


def get_carrier_accounts(api: shippo.Shippo, carrier: CarriersEnum) -> List[CarrierAccount]:
    carrier_accounts = api.carrier_accounts.list(request=ListCarrierAccountsRequest(
        carrier=carrier
    ))
    return carrier_accounts.results
