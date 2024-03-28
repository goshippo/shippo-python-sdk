import shippo
from shippo.models.components import AddressCreateRequest, CustomsDeclarationCreateRequest, \
    CustomsDeclarationCreateRequestIncoterm, CustomsItemBase, WeightUnit, CustomsDeclarationCreateRequestContentsType, \
    CustomsDeclarationCreateRequestNonDeliveryOption, ShipmentCreateRequest, ParcelCreateRequest, DistanceUnitTemplate, \
    ShipmentExtra, Insurance


# https://docs.goshippo.com/docs/stories/intl_rating_guide/
class TestPurchaseLabelInternational:

    def test_purchase_label_international(self, api: shippo.Shippo):
        create_address_response = api.addresses.create_address(
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
        assert create_address_response.address is not None

        create_customs_declaration_response = api.customs_declarations.create_customs_declaration(
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
        assert create_customs_declaration_response.customs_declaration is not None

        shipment_create_response = api.shipments.create_shipment(
            shipment_create_request=ShipmentCreateRequest(
                address_from=create_address_response.address.object_id,
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
                customs_declaration=create_customs_declaration_response.customs_declaration.object_id,
                extra=ShipmentExtra(
                    insurance=Insurance(
                        amount="200",
                        currency="USD",
                        content="guitar pedal"
                    )
                )
            ))
        assert shipment_create_response.shipment is not None