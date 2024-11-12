from typing import List

from shippo.models.components import CarriersEnum, CarrierAccount, Address
from shippo.models.operations import ListCarrierAccountsRequest

import shippo


def get_carrier_account(api: shippo.Shippo, carrier: CarriersEnum) -> CarrierAccount:
    return get_carrier_accounts(api, carrier)[0]


def get_carrier_accounts(api: shippo.Shippo, carrier: CarriersEnum) -> List[CarrierAccount]:
    carrier_accounts = api.carrier_accounts.list(request=ListCarrierAccountsRequest(
        carrier=carrier
    ))
    return carrier_accounts.results


def get_first_address_object_id(api: shippo.Shippo) -> str:
    """Get the first address object ID."""
    return get_addresses(api)[0].object_id


def get_addresses(api: shippo.Shippo) -> list[Address]:
    """Get the list of addresses."""
    return api.addresses.list().results
