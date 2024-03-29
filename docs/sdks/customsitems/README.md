# CustomsItems
(*customs_items*)

## Overview

Customs declarations are relevant information, including one or multiple customs items, you need to provide for customs clearance for your international shipments.
<SchemaDefinition schemaRef="#/components/schemas/CustomsItem"/>

### Available Operations

* [list_customs_items](#list_customs_items) - List all customs items
* [create_customs_item](#create_customs_item) - Create a new customs item
* [get_customs_item](#get_customs_item) - Retrieve a customs item

## list_customs_items

Returns a list all customs items objects.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.customs_items.list_customs_items(page=1, results=25, shippo_api_version='<value>')

if res.customs_item_paginated_list is not None:
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

**[operations.ListCustomsItemsResponse](../../models/operations/listcustomsitemsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_customs_item

Creates a new customs item object.

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.customs_items.create_customs_item(shippo_api_version='<value>', customs_item_base=components.CustomsItemBase(
    description='T-Shirt',
    mass_unit=components.WeightUnit.LB,
    net_weight='5',
    origin_country='<value>',
    quantity=20,
    value_amount='200',
    value_currency='USD',
    metadata='Order ID "123454"',
    sku_code='HM-123',
))

if res.customs_item is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `shippo_api_version`                                                               | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | String used to pick a non-default API version to use                               |
| `customs_item_base`                                                                | [Optional[components.CustomsItemBase]](../../models/components/customsitembase.md) | :heavy_minus_sign:                                                                 | CustomsItem details.                                                               |


### Response

**[operations.CreateCustomsItemResponse](../../models/operations/createcustomsitemresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_customs_item

Returns an existing customs item using an object ID

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.customs_items.get_customs_item(customs_item_id='<value>', page=1, shippo_api_version='<value>')

if res.customs_item is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `customs_item_id`                                    | *str*                                                | :heavy_check_mark:                                   | Object ID of the customs item                        |
| `page`                                               | *Optional[int]*                                      | :heavy_minus_sign:                                   | The page number you want to select                   |
| `shippo_api_version`                                 | *Optional[str]*                                      | :heavy_minus_sign:                                   | String used to pick a non-default API version to use |


### Response

**[operations.GetCustomsItemResponse](../../models/operations/getcustomsitemresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
