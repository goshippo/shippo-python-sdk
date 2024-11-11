import pytest
from dateutil.parser import isoparse

import shippo
from shippo.models.components import OrderCreateRequest, LineItemBase, WeightUnitEnum, AddressCreateRequest, \
    OrderStatusEnum, Order


class TestCreateOrder:

    @pytest.fixture
    def create_order(self, api: shippo.Shippo):
        return api.orders.create(request=OrderCreateRequest(
            placed_at='2016-09-23T01:28:12Z',
            to_address=AddressCreateRequest(
                country='US',
                name='Shwan Ippotle',
                company='Shippo',
                street1='215 Clayton St.',
                street3='',
                street_no='',
                city='San Francisco',
                state='CA',
                zip='94117',
                phone='+1 555 341 9393',
                email='shippotle@shippo.com',
                is_residential=True,
                metadata='Customer ID 123456',
                validate=True,
            ),
            currency='USD',
            notes='This customer is a VIP',
            order_number='#1068',
            order_status=OrderStatusEnum.PAID,
            shipping_cost='12.83',
            shipping_cost_currency='USD',
            shipping_method='USPS First Class Package',
            subtotal_price='12.1',
            total_price='24.93',
            total_tax='0.0',
            weight='0.4',
            weight_unit=WeightUnitEnum.LB,
            from_address=AddressCreateRequest(
                country='US',
                name='Shwan Ippotle',
                company='Shippo',
                street1='215 Clayton St.',
                street3='',
                street_no='',
                city='San Francisco',
                state='CA',
                zip='94117',
                phone='+1 555 341 9393',
                email='shippotle@shippo.com',
                is_residential=True,
                metadata='Customer ID 123456',
                validate=True,
            ),
            line_items=[
                LineItemBase(
                    currency='USD',
                    manufacture_country='US',
                    max_delivery_time=isoparse('2016-07-23T00:00:00Z'),
                    max_ship_time=isoparse('2016-07-23T00:00:00Z'),
                    quantity=20,
                    sku='HM-123',
                    title='Hippo Magazines',
                    total_price='12.1',
                    variant_title='June Edition',
                    weight='0.4',
                    weight_unit=WeightUnitEnum.LB,
                ),
            ],
        ))

    @pytest.mark.order(1)
    def test_create_order(self, create_order):
        order = create_order

        assert order is not None
        assert isinstance(order, Order)
        assert order.object_id is not None
