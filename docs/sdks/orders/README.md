# Orders
(*orders*)

## Overview

An order is a request from a customer to purchase goods from a merchant. 
Use the orders object to load orders from your system to the Shippo dashboard.
You can use the orders object to create, retrieve, list, and manage orders programmatically. 
You can also retrieve shipping rates, purchase labels, and track shipments for each order.
<SchemaDefinition schemaRef="#/components/schemas/Order"/>

# Line Item
<p style="text-align: center; background-color: #F2F3F4;">
  </br>Line Items, and their corresponding abstract Products and Variants, might be exposed as a separate resource 
  in the future. Currently it's a nested object within the order resource.</br></br>
</p>
 A line item is an individual object in an order. For example, if your order contains a t-shirt, shorts, and a jacket, each item is represented by a line item.
<SchemaDefinition schemaRef="#/components/schemas/LineItem"/>

### Available Operations

* [list](#list) - List all orders
* [create](#create) - Create a new order
* [get](#get) - Retrieve an order

## list

Returns a list of all order objects.

### Example Usage

```python
import shippo
from shippo.models import components, operations

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.orders.list(request=operations.ListOrdersRequest(
    order_status=[
        components.OrderStatusEnum.PAID,
    ],
    shop_app=components.OrderShopAppEnum.SHIPPO,
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.ListOrdersRequest](../../models/operations/listordersrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |

### Response

**[components.OrderPaginatedList](../../models/components/orderpaginatedlist.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create

Creates a new order object.

### Example Usage

```python
import dateutil.parser
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.orders.create(request=components.OrderCreateRequest(
    placed_at='2016-09-23T01:28:12Z',
    to_address=components.AddressCreateRequest(
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
    order_status=components.OrderStatusEnum.PAID,
    shipping_cost='12.83',
    shipping_cost_currency='USD',
    shipping_method='USPS First Class Package',
    subtotal_price='12.1',
    total_price='24.93',
    total_tax='0.0',
    weight='0.4',
    weight_unit=components.WeightUnitEnum.LB,
    from_address=components.AddressCreateRequest(
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
        components.LineItemBase(
            currency='USD',
            manufacture_country='US',
            max_delivery_time=dateutil.parser.isoparse('2016-07-23T00:00:00Z'),
            max_ship_time=dateutil.parser.isoparse('2016-07-23T00:00:00Z'),
            quantity=20,
            sku='HM-123',
            title='Hippo Magazines',
            total_price='12.1',
            variant_title='June Edition',
            weight='0.4',
            weight_unit=components.WeightUnitEnum.LB,
        ),
    ],
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [components.OrderCreateRequest](../../models/components/ordercreaterequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |

### Response

**[components.Order](../../models/components/order.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get

Retrieves an existing order using an object ID.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.orders.get(order_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter              | Type                   | Required               | Description            |
| ---------------------- | ---------------------- | ---------------------- | ---------------------- |
| `order_id`             | *str*                  | :heavy_check_mark:     | Object ID of the order |

### Response

**[components.Order](../../models/components/order.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |