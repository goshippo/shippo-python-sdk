import shippo
from shippo.models.components import (
    AddressCreateRequest,
    CustomsDeclarationCreateRequest,
    CustomsDeclarationIncotermEnum,
    CustomsItemCreateRequest,
    WeightUnitEnum,
    CustomsDeclarationContentsTypeEnum,
    CustomsDeclarationNonDeliveryOptionEnum,
    ShipmentCreateRequest,
    ParcelCreateRequest,
    DistanceUnitEnum,
    ShipmentExtra,
    Insurance,
)


# https://docs.goshippo.com/docs/stories/intl_rating_guide/
class TestPurchaseLabelInternational:

    def test_purchase_label_international(self, api: shippo.Shippo):
        address = api.addresses.create(
            request=AddressCreateRequest(
                name="Sarah",
                company="We Sell Guitars",
                street1="215 Clayton St.",
                city="San Francisco",
                state="CA",
                zip="94117",
                country="US",
                phone="+1 555 341 9393",
                email="sarah@wesellguitars.net",
                is_residential=False,
                metadata="We Sell Guitars HQ",
            )
        )
        assert address is not None
        assert address.object_id is not None

        customs_declaration = api.customs_declarations.create(
            request=CustomsDeclarationCreateRequest(
                contents_type=CustomsDeclarationContentsTypeEnum.MERCHANDISE,
                non_delivery_option=CustomsDeclarationNonDeliveryOptionEnum.RETURN,
                certify=True,
                certify_signer="Tom Marks",
                incoterm=CustomsDeclarationIncotermEnum.DDP,
                items=[
                    CustomsItemCreateRequest(
                        description="Guitar Pedal",
                        quantity=1,
                        net_weight="5",
                        mass_unit=WeightUnitEnum.LB,
                        value_amount="200",
                        value_currency="USD",
                        origin_country="US",
                    )
                ],
            )
        )
        assert customs_declaration is not None

        shipment = api.shipments.create(
            request=ShipmentCreateRequest(
                address_from=address.object_id,
                address_to=AddressCreateRequest(
                    name="Tom Marks",
                    street1="159 Broadhurst Gardens",
                    city="London",
                    zip="NW6 3AU",
                    country="GB",
                    phone="4159876543",
                    email="tommarks@gmmail.com",
                ),
                parcels=[
                    ParcelCreateRequest(
                        weight="5",
                        length="10",
                        width="5",
                        height="4",
                        distance_unit=DistanceUnitEnum.IN,
                        mass_unit=WeightUnitEnum.LB,
                    )
                ],
                customs_declaration=customs_declaration.object_id,
                extra=ShipmentExtra(
                    insurance=Insurance(
                        amount="200", currency="USD", content="guitar pedal"
                    )
                ),
            )
        )
        assert shipment is not None
