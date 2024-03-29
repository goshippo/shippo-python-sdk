import shippo
from shippo.models.components import Carriers, DistanceUnitTemplate, WeightUnit, \
    AddressCreateRequest, ShipmentCreateRequest, InstantTransactionRequestBody, \
    ParcelCreateRequest
from tests.helpers_custom import get_carrier_account


# https://docs.goshippo.com/docs/guides_general/single_call/
class TestInstalabel:

    def test_instalabel(self, api: shippo.Shippo):
        carrier_account = get_carrier_account(api, Carriers.USPS)

        transaction = api.transactions.create(
            request_body=InstantTransactionRequestBody(
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
                        email="rachael@alltheyarnz.com"
                    ),
                    address_to=AddressCreateRequest(
                        name="Mr Hippo",
                        street1="965 Mission St #572",
                        city="San Francisco",
                        state="CA",
                        zip="94103",
                        country="US",
                        phone="4151234567",
                        email="mrhippo@shippo.com"
                    ),
                    parcels=[
                        ParcelCreateRequest(
                            length="5",
                            width="5",
                            height="5",
                            distance_unit=DistanceUnitTemplate.CM,
                            weight="2",
                            mass_unit=WeightUnit.LB
                        )
                    ]
                )
            ))
        assert transaction is not None
