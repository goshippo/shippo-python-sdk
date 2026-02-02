# CustomsItems

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

<!-- UsageSnippet language="python" operationID="ListCustomsItems" method="get" path="/customs/items" -->
```python
from shippo import Shippo


with Shippo(
    shippo_api_version="2018-02-08",
    api_key_header="<YOUR_API_KEY_HERE>",
) as s_client:

    res = s_client.customs_items.list(page=1, results=25)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The page number you want to select                                  |
| `results`                                                           | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The number of results to return per page (max 100)                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[components.CustomsItemPaginatedList](../../models/components/customsitempaginatedlist.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create

Creates a new customs item object.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateCustomsItem" method="post" path="/customs/items" -->
```python
from shippo import Shippo
from shippo.models import components


with Shippo(
    shippo_api_version="2018-02-08",
    api_key_header="<YOUR_API_KEY_HERE>",
) as s_client:

    res = s_client.customs_items.create(request={
        "description": "T-Shirt",
        "mass_unit": components.WeightUnitEnum.LB,
        "metadata": "Order ID \"123454\"",
        "net_weight": "5",
        "origin_country": "<value>",
        "quantity": 20,
        "sku_code": "HM-123",
        "hs_code": "0901.21",
        "value_amount": "200",
        "value_currency": "USD",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [components.CustomsItemCreateRequest](../../models/components/customsitemcreaterequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[components.CustomsItem](../../models/components/customsitem.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get

Returns an existing customs item using an object ID

### Example Usage

<!-- UsageSnippet language="python" operationID="GetCustomsItem" method="get" path="/customs/items/{CustomsItemId}" -->
```python
from shippo import Shippo


with Shippo(
    shippo_api_version="2018-02-08",
    api_key_header="<YOUR_API_KEY_HERE>",
) as s_client:

    res = s_client.customs_items.get(customs_item_id="<id>", page=1)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `customs_item_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | Object ID of the customs item                                       |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The page number you want to select                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[components.CustomsItem](../../models/components/customsitem.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |