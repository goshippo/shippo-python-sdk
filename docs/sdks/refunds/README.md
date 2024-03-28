# Refunds
(*refunds*)

## Overview

Refunds are reimbursements for successfully created but unused shipping labels or other charges.
<SchemaDefinition schemaRef="#/components/schemas/Refund"/>

### Available Operations

* [create_refund](#create_refund) - Create a refund
* [list_refund](#list_refund) - List all refunds
* [get_refund](#get_refund) - Retrieve a refund

## create_refund

Creates a new refund object.

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.refunds.create_refund(shippo_api_version='<value>', refund_request_body=components.RefundRequestBody(
    transaction='915d94940ea54c3a80cbfa328722f5a1',
    async_=False,
))

if res.refund is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `shippo_api_version`                                                                   | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | String used to pick a non-default API version to use                                   |
| `refund_request_body`                                                                  | [Optional[components.RefundRequestBody]](../../models/components/refundrequestbody.md) | :heavy_minus_sign:                                                                     | Refund details                                                                         |


### Response

**[operations.CreateRefundResponse](../../models/operations/createrefundresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_refund

Returns a list all refund objects.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.refunds.list_refund(shippo_api_version='<value>')

if res.refund_paginated_list is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `shippo_api_version`                                 | *Optional[str]*                                      | :heavy_minus_sign:                                   | String used to pick a non-default API version to use |


### Response

**[operations.ListRefundResponse](../../models/operations/listrefundresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_refund

Returns an existing rate using a rate object ID.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.refunds.get_refund(refund_id='<value>', shippo_api_version='<value>')

if res.refund is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `refund_id`                                          | *str*                                                | :heavy_check_mark:                                   | Object ID of the refund to update                    |
| `shippo_api_version`                                 | *Optional[str]*                                      | :heavy_minus_sign:                                   | String used to pick a non-default API version to use |


### Response

**[operations.GetRefundResponse](../../models/operations/getrefundresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
