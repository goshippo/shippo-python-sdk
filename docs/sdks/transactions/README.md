# Transactions
(*transactions*)

## Overview

A transaction is the purchase of a shipping label from a shipping provider for a specific service. You can print purchased labels and used them to ship a parcel with a carrier, such as USPS or FedEx.
<SchemaDefinition schemaRef="#/components/schemas/Transaction"/>

### Available Operations

* [list_transactions](#list_transactions) - List all shipping labels
* [create_transaction](#create_transaction) - Create a shipping label
* [get_transaction](#get_transaction) - Retrieve a shipping label

## list_transactions

Returns a list of all transaction objects.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.transactions.list_transactions(page=1, results=25, shippo_api_version='<value>')

if res.transaction_list_wrapper is not None:
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

**[operations.ListTransactionsResponse](../../models/operations/listtransactionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_transaction

Creates a new transaction object and purchases the shipping label using a rate object that has previously been created. <br> OR <br> Creates a new transaction object and purchases the shipping label instantly using shipment details, an existing carrier account, and an existing service level token.

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.transactions.create_transaction(shippo_api_version='<value>', request_body=components.TransactionCreateRequest(
    rate='ec9f0d3adc9441449c85d315f0997fd5',
    async_=False,
    label_file_type=components.LabelFileType.PDF_4X6,
    metadata='Order ID #12345',
))

if res.transaction is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                 | Type                                                                                                                                                      | Required                                                                                                                                                  | Description                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `shippo_api_version`                                                                                                                                      | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | String used to pick a non-default API version to use                                                                                                      |
| `request_body`                                                                                                                                            | [Optional[Union[components.TransactionCreateRequest, components.InstantTransactionRequestBody]]](../../models/operations/createtransactionrequestbody.md) | :heavy_minus_sign:                                                                                                                                        | Examples.                                                                                                                                                 |


### Response

**[operations.CreateTransactionResponse](../../models/operations/createtransactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_transaction

Returns an existing transaction using an object ID.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.transactions.get_transaction(transaction_id='<value>', shippo_api_version='<value>')

if res.transaction is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `transaction_id`                                     | *str*                                                | :heavy_check_mark:                                   | Object ID of the transaction to update               |
| `shippo_api_version`                                 | *Optional[str]*                                      | :heavy_minus_sign:                                   | String used to pick a non-default API version to use |


### Response

**[operations.GetTransactionResponse](../../models/operations/gettransactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
