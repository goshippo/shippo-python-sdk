import pytest

import shippo
from shippo.models.components import (
    CarriersEnum,
    DistanceUnitEnum,
    WeightUnitEnum,
    AddressCreateRequest,
    ParcelCreateRequest,
    ShipmentCreateRequest,
    InstantTransactionCreateRequest,
    Transaction,
)
from shippo.models.components.corerate import CoreRate
from tests.helpers_custom import get_carrier_account


# https://docs.goshippo.com/docs/guides_general/single_call/
class TestInstalabel:

    def test_instalabel(self, api: shippo.Shippo):
        carrier_account = get_carrier_account(api, CarriersEnum.USPS)

        if carrier_account.object_id is None:
            pytest.fail("The created carrier_account must have an object_id")

        request = InstantTransactionCreateRequest(
            carrier_account=carrier_account.object_id,
            servicelevel_token="usps_ground_advantage",
            shipment=ShipmentCreateRequest(
                address_from=AddressCreateRequest(
                    name="Rachael",
                    street1="1092 Indian Summer Ct",
                    city="San Jose",
                    state="CA",
                    zip="95122",
                    country="US",
                    phone="4159876543",
                    email="rachael@alltheyarnz.com",
                ),
                address_to=AddressCreateRequest(
                    name="Mr Hippo",
                    street1="965 Mission St #572",
                    city="San Francisco",
                    state="CA",
                    zip="94103",
                    country="US",
                    phone="4151234567",
                    email="mrhippo@shippo.com",
                ),
                parcels=[
                    ParcelCreateRequest(
                        length="5",
                        width="5",
                        height="5",
                        distance_unit=DistanceUnitEnum.CM,
                        weight="2",
                        mass_unit=WeightUnitEnum.LB,
                    )
                ],
            ),
        )

        transaction = api.transactions.create(request=request)

        assert transaction is not None
        assert isinstance(transaction, Transaction)
        assert transaction.rate is not None
        assert isinstance(transaction.rate, CoreRate)
        assert transaction.rate.object_id is not None
