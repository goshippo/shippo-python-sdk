import pytest

import shippo
from shippo.models.components import ServiceGroupCreateRequest, Carriers, \
    ServiceGroupAccountAndServiceLevel, ServiceGroupType, LiveRateCreateRequest, AddressCompleteCreateRequest, \
    LineItem, WeightUnit, Parcel, DistanceUnitTemplate
from tests.helpers_custom import get_carrier_account


class TestRatesAtCheckout:

    @pytest.fixture(scope='class', autouse=True)
    def setup(self, api: shippo.Shippo):
        self._delete_all_service_groups(api)

    def _delete_all_service_groups(self, api: shippo.Shippo):
        response = api.service_groups.list_service_groups()
        for sg in response.service_group_list_response:
            api.service_groups.delete_service_group(sg.object_id)

    def test_rates_at_checkout(self, api: shippo.Shippo):
        carrier_account = get_carrier_account(api, Carriers.USPS)
        ups_account_id = carrier_account.object_id

        # TODO: update spec so that ServiceLevel* enum models are generated
        available_service_levels = ["ups_ground", "ups_next_day_air_saver"]
        service_levels = [
            ServiceGroupAccountAndServiceLevel(
                account_object_id=ups_account_id,
                service_level_token=available_service_level
            )
            for available_service_level in available_service_levels
        ]

        create_service_group_response = api.service_groups.create_service_group(
            service_group_create_request=ServiceGroupCreateRequest(
                name="UPS shipping",
                description="UPS shipping options",
                flat_rate="5",
                flat_rate_currency="USD",
                type=ServiceGroupType.LIVE_RATE,
                service_levels=service_levels
            ))
        assert create_service_group_response.service_group is not None

        response = api.rates_at_checkout.create_live_rate(
            live_rate_create_request=LiveRateCreateRequest(
                address_from=AddressCompleteCreateRequest(
                    name="S. Hippo",
                    company="Shippo",
                    street1="731 Market St #200",
                    city="San Francisco",
                    state="CA",
                    zip="94103",
                    country="US"
                ),
                address_to=AddressCompleteCreateRequest(
                    name="Bob Bloat",
                    company="SF Zoo",
                    street1="Sloat Blvd. & Upper Great Hwy.",
                    city="San Francisco",
                    state="CA",
                    zip="94132",
                    country="US"
                ),
                line_items=[
                    LineItem(
                        quantity=1,
                        total_price="12.00",
                        currency="USD",
                        weight="1.0",
                        weight_unit=WeightUnit.LB,
                        title="Hippo Snax",
                        manufacture_country="US",
                        sku="HM-123"
                    )
                ],
                parcel=Parcel(
                    length="10",
                    width="15",
                    height="10",
                    distance_unit=DistanceUnitTemplate.IN,
                    weight="1",
                    mass_unit=WeightUnit.LB
                )
            ))
        assert len(response.live_rate_paginated_list.results) > 0
        for live_rate in response.live_rate_paginated_list.results:
            assert live_rate.title == create_service_group_response.service_group.name
