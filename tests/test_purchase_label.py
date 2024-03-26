import shippo
from shippo.models.components import Carriers, ParcelRequest, DistanceUnitTemplate, WeightUnit, \
    AddressCreateRequest, ShipmentCreateRequest, TransactionCreateRequest, ParcelCreateRequest
from tests.helpers_custom import get_carrier_accounts


class TestPurchaseLabel:

    def test_purchase_label(self, api: shippo.Shippo):
        carrier_accounts = get_carrier_accounts(api, Carriers.USPS)
        carrier_account_ids = [carrier_account.object_id for carrier_account in carrier_accounts]

        create_shipment_response = api.shipments.create_shipment(
            shipment_create_request=ShipmentCreateRequest(
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
                ],
                carrier_accounts=carrier_account_ids
            ))
        assert create_shipment_response.shipment is not None

        shipment = create_shipment_response.shipment
        create_transaction_response = api.transactions.create_transaction(
            request_body=TransactionCreateRequest(rate=shipment.rates[0].object_id)
        )
        assert create_transaction_response.transaction is not None

    def test_purchase_label_using_reference_ids(self, api: shippo.Shippo):
        create_address_from_response = api.addresses.create_address(
            address_create_request=AddressCreateRequest(
                name="Rachael",
                street1="1092 Indian Summer Ct",
                city="San Jose",
                state="CA",
                zip="95122",
                country="US",
                phone="4159876543",
                email="rachael@alltheyarnz.com"
            ))
        address_from = create_address_from_response.address

        create_address_to_response = api.addresses.create_address(
            address_create_request=AddressCreateRequest(
                name="Mr Hippo",
                street1="965 Mission St #572",
                city="San Francisco",
                state="CA",
                zip="94103",
                country="US",
                phone="4151234567",
                email="mrhippo@shippo.com"
            ))
        address_to = create_address_to_response.address

        create_parcel_response = api.parcels.create_parcel(
            parcel_request=ParcelRequest(
                length="5",
                width="5",
                height="5",
                distance_unit=DistanceUnitTemplate.CM,
                weight="2",
                mass_unit=WeightUnit.LB,
                metadata="Wool Box1",
            ))
        parcel = create_parcel_response.parcel

        create_shipment_response = api.shipments.create_shipment(
            shipment_create_request=ShipmentCreateRequest(
                address_from=address_from.object_id,
                address_return=address_from.object_id,
                address_to=address_to.object_id,
                parcels=[parcel.object_id]
            ))
        assert create_shipment_response.shipment is not None
        shipment = create_shipment_response.shipment
        assert shipment.address_to.object_id == address_to.object_id
        assert shipment.address_from.object_id == address_from.object_id
        assert shipment.address_return.object_id == address_from.object_id

        create_transaction_response = api.transactions.create_transaction(
            request_body=TransactionCreateRequest(rate=shipment.rates[0].object_id)
        )
        assert create_transaction_response.transaction is not None
