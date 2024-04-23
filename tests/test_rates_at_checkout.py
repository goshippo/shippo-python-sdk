import pytest

import shippo
from shippo.models.components import ServiceGroupCreateRequest, CarriersEnum, \
    ServiceGroupAccountAndServiceLevel, ServiceGroupTypeEnum, LiveRateCreateRequest, AddressCompleteCreateRequest, \
    LineItem, WeightUnitEnum, Parcel, DistanceUnitEnum, ServiceLevelUPSEnum
from tests.helpers_custom import get_carrier_account


class TestRatesAtCheckout:

    @pytest.fixture(scope='class', autouse=True)
    def setup(self, api: shippo.Shippo):
        self._delete_all_service_groups(api)

    def _delete_all_service_groups(self, api: shippo.Shippo):
        service_groups = api.service_groups.list()
        for sg in service_groups:
            api.service_groups.delete(sg.object_id)

    def test_rates_at_checkout(self, api: shippo.Shippo):
        carrier_account = get_carrier_account(api, CarriersEnum.UPS)
        ups_account_id = carrier_account.object_id

        available_service_levels = [ServiceLevelUPSEnum.UPS_GROUND, ServiceLevelUPSEnum.UPS_NEXT_DAY_AIR_SAVER]
        service_levels = [
            ServiceGroupAccountAndServiceLevel(
                account_object_id=ups_account_id,
                service_level_token=available_service_level.value
            )
            for available_service_level in available_service_levels
        ]

        service_group = api.service_groups.create(
            ServiceGroupCreateRequest(
                name="UPS shipping",
                description="UPS shipping options",
                flat_rate="5",
                flat_rate_currency="USD",
                type=ServiceGroupTypeEnum.LIVE_RATE,
                service_levels=service_levels
            ))
        assert service_group is not None

        live_rates = api.rates_at_checkout.create(
            LiveRateCreateRequest(
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
                        weight_unit=WeightUnitEnum.LB,
                        title="Hippo Snax",
                        manufacture_country="US",
                        sku="HM-123"
                    )
                ],
                parcel=Parcel(
                    length="10",
                    width="15",
                    height="10",
                    distance_unit=DistanceUnitEnum.IN,
                    weight="1",
                    mass_unit=WeightUnitEnum.LB
                )
            ))
        assert len(live_rates.results) > 0
        for live_rate in live_rates.results:
            assert live_rate.title == service_group.name
