# Refunds
(*refunds*)

## Overview

Refunds are reimbursements for successfully created but unused shipping labels or other charges.
<SchemaDefinition schemaRef="#/components/schemas/Refund"/>

### Available Operations

* [create](#create) - Create a refund
* [list](#list) - List all refunds
* [get](#get) - Retrieve a refund

## create

Creates a new refund object.

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.refunds.create(request=components.RefundRequestBody(
    transaction='915d94940ea54c3a80cbfa328722f5a1',
    async_=False,
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                        | Type                             | Required                         | Description                      | Example                          |
| -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- |
| `transaction`                    | *str*                            | :heavy_check_mark:               | N/A                              | 915d94940ea54c3a80cbfa328722f5a1 |
| `async_`                         | *Optional[bool]*                 | :heavy_minus_sign:               | N/A                              | false                            |

### Response

**[components.Refund](../../models/components/refund.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |


## list

Returns a list all refund objects.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.refunds.list()

if res is not None:
    # handle response
    pass

```

### Response

**[components.RefundPaginatedList](../../models/components/refundpaginatedlist.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |


## get

Returns an existing rate using a rate object ID.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.refunds.get(refund_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                         | Type                              | Required                          | Description                       |
| --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- |
| `refund_id`                       | *str*                             | :heavy_check_mark:                | Object ID of the refund to update |

### Response

**[components.Refund](../../models/components/refund.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
