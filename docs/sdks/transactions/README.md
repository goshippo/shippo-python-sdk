# Transactions
(*transactions*)

## Overview

A transaction is the purchase of a shipping label from a shipping provider for a specific service. You can print purchased labels and used them to ship a parcel with a carrier, such as USPS or FedEx.
<SchemaDefinition schemaRef="#/components/schemas/Transaction"/>

### Available Operations

* [list](#list) - List all shipping labels
* [create](#create) - Create a shipping label
* [get](#get) - Retrieve a shipping label

## list

Returns a list of all transaction objects.

### Example Usage

```python
import shippo
from shippo.models import components, operations

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.transactions.list(request=operations.ListTransactionsRequest(
    object_status=components.TransactionStatusEnum.SUCCESS,
    tracking_status=components.TrackingStatusEnum.DELIVERED,
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListTransactionsRequest](../../models/operations/listtransactionsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |

### Response

**[components.TransactionPaginatedList](../../models/components/transactionpaginatedlist.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |


## create

Creates a new transaction object and purchases the shipping label using a rate object that has previously been created. <br> OR <br> Creates a new transaction object and purchases the shipping label instantly using shipment details, an existing carrier account, and an existing service level token.

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.transactions.create(request=components.TransactionCreateRequest(
    rate='ec9f0d3adc9441449c85d315f0997fd5',
    async_=False,
    label_file_type=components.LabelFileTypeEnum.PDF_4X6,
    metadata='Order ID #12345',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateTransactionRequestBody](../../models/operations/createtransactionrequestbody.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |

### Response

**[components.Transaction](../../models/components/transaction.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |


## get

Returns an existing transaction using an object ID.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.transactions.get(transaction_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                              | Type                                   | Required                               | Description                            |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| `transaction_id`                       | *str*                                  | :heavy_check_mark:                     | Object ID of the transaction to update |

### Response

**[components.Transaction](../../models/components/transaction.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
