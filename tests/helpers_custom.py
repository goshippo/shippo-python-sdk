import string
from typing import List

from shippo.models.components import CarriersEnum, CarrierAccount, Order
from shippo.models.operations import ListCarrierAccountsRequest, ListOrdersRequest

import shippo


def get_carrier_account(api: shippo.Shippo, carrier: CarriersEnum) -> CarrierAccount:
    return get_carrier_accounts(api, carrier)[0]


def get_carrier_accounts(api: shippo.Shippo, carrier: CarriersEnum) -> List[CarrierAccount]:
    carrier_accounts = api.carrier_accounts.list(request=ListCarrierAccountsRequest(
        carrier=carrier
    ))
    return carrier_accounts.results


def get_order_object_id(api: shippo.Shippo) -> string:
    orders = api.orders.list(request=ListOrdersRequest())
    return orders.results[0].object_id
