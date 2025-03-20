from typing import Any, List
from typing_extensions import TypeGuard

import shippo
from shippo.models.components import CarriersEnum
from shippo.models.components.carrieraccountwithextrainfo import (
    CarrierAccountWithExtraInfo,
)
from shippo.models.operations import ListCarrierAccountsRequest


def get_carrier_account(
    api: shippo.Shippo, carrier: CarriersEnum
) -> CarrierAccountWithExtraInfo:
    return get_carrier_accounts(api, carrier)[0]


def get_carrier_accounts(
    api: shippo.Shippo, carrier: CarriersEnum
) -> List[CarrierAccountWithExtraInfo]:
    carrier_accounts = api.carrier_accounts.list(
        request=ListCarrierAccountsRequest(carrier=carrier)
    )

    if carrier_accounts is None or carrier_accounts.results is None:
        raise ValueError(f"Carrier accounts for {carrier} not found")

    return carrier_accounts.results


def is_str_list(lst: List[Any]) -> TypeGuard[List[str]]:
    """Check if the list is a list of strings."""
    return isinstance(lst, list) and all(isinstance(i, str) for i in lst)
