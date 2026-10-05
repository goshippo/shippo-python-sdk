# Transactions

## Overview

A transaction is the purchase of a shipping label from a shipping provider for a specific service. You can print purchased labels and used them to ship a parcel with a carrier, such as USPS or FedEx.

### Available Operations

* [list](#list) - List all shipping labels
* [create](#create) - Create a shipping label
* [get](#get) - Retrieve a shipping label

## list

Returns a list of all transaction objects.

To filter results by creation date, use the optional query parameters below. Provided dates should be ISO 8601 UTC dates (timezone offsets are currently not supported).

- `object_created_gt`: object(s) created after the provided date time
- `object_created_gte`: object(s) created at or after the provided date time
- `object_created_lt`: object(s) created before the provided date time
- `object_created_lte`: object(s) created at or before the provided date time

Provide at most one lower bound (`object_created_gt` or `object_created_gte`) and at most one upper bound (`object_created_lt` or `object_created_lte`) per request. Lower bounds must not be in the future.

Date format examples: `2017-01-01`, `2017-01-01T03:30:30` (or `2017-01-01T03:30:30.5`), `2017-01-01T03:30:30Z`

Example URL: `https://api.goshippo.com/transactions/?object_created_gte=2017-01-01T00:00:30&object_created_lt=2017-04-01T00:00:30`

### Example Usage

<!-- UsageSnippet language="python" operationID="ListTransactions" method="get" path="/transactions" -->
```python
from shippo import Shippo
from shippo.models import components


with Shippo(
    shippo_api_version="2018-02-08",
    api_key_header="<YOUR_API_KEY_HERE>",
) as s_client:

    res = s_client.transactions.list(request={
        "object_status": components.TransactionStatusEnum.SUCCESS,
        "tracking_status": components.TrackingStatusEnum.DELIVERED,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListTransactionsRequest](../../models/operations/listtransactionsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[components.TransactionPaginatedList](../../models/components/transactionpaginatedlist.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create

Creates a new transaction object and purchases the shipping label using a rate object that has previously been created.

Alternatively, creates a new transaction object and purchases the shipping label instantly using shipment details, an existing carrier account, and an existing service level token.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateTransaction" method="post" path="/transactions" -->
```python
from shippo import Shippo
from shippo.models import components


with Shippo(
    shippo_api_version="2018-02-08",
    api_key_header="<YOUR_API_KEY_HERE>",
) as s_client:

    res = s_client.transactions.create(request={
        "async_": False,
        "label_file_type": components.LabelFileTypeEnum.PDF_4X6,
        "metadata": "Order ID #12345",
        "rate": "ec9f0d3adc9441449c85d315f0997fd5",
        "order": "adcfdddf8ec64b84ad22772bce3ea37a",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateTransactionRequest](../../models/operations/createtransactionrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[components.Transaction](../../models/components/transaction.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get

Returns an existing transaction using an object ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetTransaction" method="get" path="/transactions/{TransactionId}" -->
```python
from shippo import Shippo


with Shippo(
    shippo_api_version="2018-02-08",
    api_key_header="<YOUR_API_KEY_HERE>",
) as s_client:

    res = s_client.transactions.get(transaction_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `transaction_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | Object ID of the transaction to update                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[components.Transaction](../../models/components/transaction.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |