# CustomsItems
(*customs_items*)

## Overview

Customs declarations are relevant information, including one or multiple customs items, you need to provide for customs clearance for your international shipments.
<SchemaDefinition schemaRef="#/components/schemas/CustomsItem"/>

### Available Operations

* [list](#list) - List all customs items
* [create](#create) - Create a new customs item
* [get](#get) - Retrieve a customs item

## list

Returns a list all customs items objects.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.customs_items.list()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                          | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `page`                                             | *Optional[int]*                                    | :heavy_minus_sign:                                 | The page number you want to select                 |
| `results`                                          | *Optional[int]*                                    | :heavy_minus_sign:                                 | The number of results to return per page (max 100) |

### Response

**[components.CustomsItemPaginatedList](../../models/components/customsitempaginatedlist.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create

Creates a new customs item object.

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.customs_items.create(request=components.CustomsItemCreateRequest(
    description='T-Shirt',
    mass_unit=components.WeightUnitEnum.LB,
    net_weight='5',
    origin_country='<value>',
    quantity=20,
    value_amount='200',
    value_currency='USD',
    metadata='Order ID "123454"',
    sku_code='HM-123',
    hs_code='0901.21',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [components.CustomsItemCreateRequest](../../models/components/customsitemcreaterequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |

### Response

**[components.CustomsItem](../../models/components/customsitem.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get

Returns an existing customs item using an object ID

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.customs_items.get(customs_item_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                          | Type                               | Required                           | Description                        |
| ---------------------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- |
| `customs_item_id`                  | *str*                              | :heavy_check_mark:                 | Object ID of the customs item      |
| `page`                             | *Optional[int]*                    | :heavy_minus_sign:                 | The page number you want to select |

### Response

**[components.CustomsItem](../../models/components/customsitem.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |