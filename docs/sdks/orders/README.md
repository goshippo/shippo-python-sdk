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

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.orders.list(page=1, results=25, shippo_api_version='<value>')

if res.order_paginated_list is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `page`                                               | *Optional[int]*                                      | :heavy_minus_sign:                                   | The page number you want to select                   |
| `results`                                            | *Optional[int]*                                      | :heavy_minus_sign:                                   | The number of results to return per page (max 100)   |
| `shippo_api_version`                                 | *Optional[str]*                                      | :heavy_minus_sign:                                   | String used to pick a non-default API version to use |


### Response

**[operations.ListOrdersResponse](../../models/operations/listordersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create

Creates a new order object.

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.orders.create(shippo_api_version='<value>', order_create_request=components.OrderCreateRequest(
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
    order_status=components.OrderCreateRequestOrderStatus.PAID,
    shipping_cost='12.83',
    shipping_cost_currency='USD',
    shipping_method='USPS First Class Package',
    subtotal_price='12.1',
    total_price='24.93',
    total_tax='0.0',
    weight='0.4',
    weight_unit=components.WeightUnit.LB,
))

if res.order is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `shippo_api_version`                                                                     | *Optional[str]*                                                                          | :heavy_minus_sign:                                                                       | String used to pick a non-default API version to use                                     |
| `order_create_request`                                                                   | [Optional[components.OrderCreateRequest]](../../models/components/ordercreaterequest.md) | :heavy_minus_sign:                                                                       | Order details.                                                                           |


### Response

**[operations.CreateOrderResponse](../../models/operations/createorderresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get

Retrieves an existing order using an object ID.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.orders.get(order_id='<value>', shippo_api_version='<value>')

if res.order is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `order_id`                                           | *str*                                                | :heavy_check_mark:                                   | Object ID of the order                               |
| `shippo_api_version`                                 | *Optional[str]*                                      | :heavy_minus_sign:                                   | String used to pick a non-default API version to use |


### Response

**[operations.GetOrderResponse](../../models/operations/getorderresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
