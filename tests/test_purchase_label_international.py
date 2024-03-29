import pytest

import shippo
from shippo.models.components import AddressCreateRequest, CustomsDeclarationCreateRequest, \
    CustomsDeclarationCreateRequestIncoterm, CustomsItemBase, WeightUnit, CustomsDeclarationCreateRequestContentsType, \
    CustomsDeclarationCreateRequestNonDeliveryOption, ShipmentCreateRequest, ParcelCreateRequest, DistanceUnitTemplate, \
    ShipmentExtra, Insurance


# https://docs.goshippo.com/docs/stories/intl_rating_guide/
class TestPurchaseLabelInternational:

    @pytest.mark.skip(reason="API returns '' for documented enum values and this test will always fail - need to update the spec")
    def test_purchase_label_international(self, api: shippo.Shippo):
        address = api.addresses.create(
            address_create_request=AddressCreateRequest(
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
                metadata="We Sell Guitars HQ"
            ))
        assert address.address is not None

        customs_declaration = api.customs_declarations.create(
            customs_declaration_create_request=CustomsDeclarationCreateRequest(
                contents_type=CustomsDeclarationCreateRequestContentsType.MERCHANDISE,
                non_delivery_option=CustomsDeclarationCreateRequestNonDeliveryOption.RETURN,
                certify=True,
                certify_signer="Tom Marks",
                incoterm=CustomsDeclarationCreateRequestIncoterm.DDP,
                items=[
                    CustomsItemBase(
                        description="Guitar Pedal",
                        quantity=1,
                        net_weight="5",
                        mass_unit=WeightUnit.LB,
                        value_amount="200",
                        value_currency="USD",
                        origin_country="US"
                    )
                ]
            ))
        assert customs_declaration is not None

        shipment = api.shipments.create(
            shipment_create_request=ShipmentCreateRequest(
                address_from=address.object_id,
                address_to=AddressCreateRequest(
                    name="Tom Marks",
                    street1="159 Broadhurst Gardens",
                    city="London",
                    zip="NW6 3AU",
                    country="GB",
                    phone="4159876543",
                    email="tommarks@gmmail.com"
                ),
                parcels=[
                    ParcelCreateRequest(
                        weight="5",
                        length="10",
                        width="5",
                        height="4",
                        distance_unit=DistanceUnitTemplate.IN,
                        mass_unit=WeightUnit.LB
                    )
                ],
                customs_declaration=customs_declaration.object_id,
                extra=ShipmentExtra(
                    insurance=Insurance(
                        amount="200",
                        currency="USD",
                        content="guitar pedal"
                    )
                )
            ))
        assert shipment is not None
