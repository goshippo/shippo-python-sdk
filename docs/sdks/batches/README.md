# Batches

## Overview

A batch is a technique for creating multiple labels at once. Use the  batch object to create and purchase many shipments in two API calls. After creating the batch, retrieve the batch to verify that all shipments are valid. You can add and remove shipments after you have created the batch. When all shipments are valid you can purchase the batch and retrieve all the shipping labels.
<SchemaDefinition schemaRef="#/components/schemas/Batch"/>

# Batch Shipment
The batch shipment object is a wrapper around a shipment object, which include shipment-specific information 
for batch processing.

Note: batch shipments can only be created on the batch endpoint, either when creating a batch object or by through 
the `/batches/{BATCH_OBJECT_ID}/add_shipments` endpoint
<SchemaDefinition schemaRef="#/components/schemas/BatchShipment"/>

### Available Operations

* [create](#create) - Create a batch
* [get](#get) - Retrieve a batch
* [add_shipments](#add_shipments) - Add shipments to a batch
* [purchase](#purchase) - Purchase a batch
* [remove_shipments](#remove_shipments) - Remove shipments from a batch

## create

Creates a new batch object for purchasing shipping labels for many shipments at once. Batches are created asynchronously. This means that the API response won't include your batch shipments yet. You need to retrieve the batch later to verify that all batch shipments are valid.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateBatch" method="post" path="/batches" -->
```python
from shippo import Shippo
from shippo.models import components


with Shippo(
    shippo_api_version="2018-02-08",
    api_key_header="<YOUR_API_KEY_HERE>",
) as s_client:

    res = s_client.batches.create(request={
        "default_carrier_account": "078870331023437cb917f5187429b093",
        "default_servicelevel_token": "usps_priority",
        "label_filetype": components.LabelFileTypeEnum.PDF_4X6,
        "metadata": "BATCH #1",
        "batch_shipments": [],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [components.BatchCreateRequest](../../models/components/batchcreaterequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[components.Batch](../../models/components/batch.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get

Returns a batch using an object ID. <br> Batch shipments are displayed 100 at a time.  You can iterate 
through each `page` using the `?page= query` parameter.  You can also filter based on batch shipment 
status, for example, by passing a query param like `?object_results=creation_failed`. <br> 
For more details on filtering results, see our guide on <a href="https://docs.goshippo.com/docs/api_concepts/filtering/" target="blank"> filtering</a>.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetBatch" method="get" path="/batches/{BatchId}" -->
```python
from shippo import Shippo


with Shippo(
    shippo_api_version="2018-02-08",
    api_key_header="<YOUR_API_KEY_HERE>",
) as s_client:

    res = s_client.batches.get(batch_id="<id>", page=1, results=5)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `batch_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Object ID of the batch                                              |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The page number you want to select                                  |
| `results`                                                           | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The number of results to return per page (max 100, default 5)       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[components.Batch](../../models/components/batch.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## add_shipments

Adds batch shipments to an existing batch.

### Example Usage

<!-- UsageSnippet language="python" operationID="AddShipmentsToBatch" method="post" path="/batches/{BatchId}/add_shipments" -->
```python
from shippo import Shippo
from shippo.models import components


with Shippo(
    shippo_api_version="2018-02-08",
    api_key_header="<YOUR_API_KEY_HERE>",
) as s_client:

    res = s_client.batches.add_shipments(batch_id="<id>", request_body=[
        components.BatchShipmentCreateRequest(
            carrier_account="a4391cd4ab974f478f55dc08b5c8e3b3",
            metadata="SHIPMENT #1",
            servicelevel_token="fedex_ground",
            shipment=components.ShipmentCreateRequest(
                extra=components.ShipmentExtra(
                    accounts_receivable_customer_account=components.UPSReferenceFields(
                        prefix="ABC",
                        value="value",
                        ref_sort=1,
                    ),
                    appropriation_number=components.UPSReferenceFields(
                        prefix="ABC",
                        value="value",
                        ref_sort=1,
                    ),
                    bill_of_lading_number=components.UPSReferenceFields(
                        prefix="ABC",
                        value="value",
                        ref_sort=1,
                    ),
                    cod=components.Cod(
                        amount="5.5",
                        currency="USD",
                        payment_method=components.PaymentMethod.CASH,
                    ),
                    cod_number=components.UPSReferenceFields(
                        prefix="ABC",
                        value="value",
                        ref_sort=1,
                    ),
                    customer_reference=components.CustomerReference(
                        ref_sort=1,
                    ),
                    dealer_order_number=components.UPSReferenceFields(
                        prefix="ABC",
                        value="value",
                        ref_sort=1,
                    ),
                    dept_number=components.DepartmentNumber(
                        ref_sort=3,
                    ),
                    fda_product_code=components.UPSReferenceFields(
                        prefix="ABC",
                        value="value",
                        ref_sort=1,
                    ),
                    insurance=components.Insurance(
                        amount="5.5",
                        currency="USD",
                    ),
                    invoice_number=components.InvoiceNumber(
                        ref_sort=2,
                    ),
                    manifest_number=components.UPSReferenceFields(
                        prefix="ABC",
                        value="value",
                        ref_sort=1,
                    ),
                    model_number=components.UPSReferenceFields(
                        prefix="ABC",
                        value="value",
                        ref_sort=1,
                    ),
                    part_number=components.UPSReferenceFields(
                        prefix="ABC",
                        value="value",
                        ref_sort=1,
                    ),
                    po_number=components.PoNumber(
                        ref_sort=2,
                    ),
                    production_code=components.UPSReferenceFields(
                        prefix="ABC",
                        value="value",
                        ref_sort=1,
                    ),
                    purchase_request_number=components.UPSReferenceFields(
                        prefix="ABC",
                        value="value",
                        ref_sort=1,
                    ),
                    rma_number=components.RmaNumber(
                        ref_sort=1,
                    ),
                    salesperson_number=components.UPSReferenceFields(
                        prefix="ABC",
                        value="value",
                        ref_sort=1,
                    ),
                    serial_number=components.UPSReferenceFields(
                        prefix="ABC",
                        value="value",
                        ref_sort=1,
                    ),
                    store_number=components.UPSReferenceFields(
                        prefix="ABC",
                        value="value",
                        ref_sort=1,
                    ),
                    transaction_reference_number=components.UPSReferenceFields(
                        prefix="ABC",
                        value="value",
                        ref_sort=1,
                    ),
                ),
                metadata="Customer ID 123456",
                shipment_date="2021-03-22T12:00:00Z",
                address_from="d799c2679e644279b59fe661ac8fa488",
                address_return="d799c2679e644279b59fe661ac8fa488",
                address_to="d799c2679e644279b59fe661ac8fa489",
                customs_declaration="adcfdddf8ec64b84ad22772bce3ea37a",
                carrier_accounts=[
                    "065a4a8c10d24a34ab932163a1b87f52",
                    "73f706f4bdb94b54a337563840ce52b0",
                ],
                parcels=[
                    "<value>",
                ],
            ),
        ),
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `batch_id`                                                                                           | *str*                                                                                                | :heavy_check_mark:                                                                                   | Object ID of the batch                                                                               |
| `request_body`                                                                                       | List[[components.BatchShipmentCreateRequest](../../models/components/batchshipmentcreaterequest.md)] | :heavy_check_mark:                                                                                   | Array of shipments to add to the batch                                                               |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[components.Batch](../../models/components/batch.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## purchase

Purchases an existing batch with a status of `VALID`. 
Once you send a POST request to the purchase endpoint the batch status will change to `PURCHASING`. 
When all the shipments are purchased, the status will change to `PURCHASED` and you will receive a 
`batch_purchased` webhook indicating that the batch has been purchased

### Example Usage

<!-- UsageSnippet language="python" operationID="PurchaseBatch" method="post" path="/batches/{BatchId}/purchase" -->
```python
from shippo import Shippo


with Shippo(
    shippo_api_version="2018-02-08",
    api_key_header="<YOUR_API_KEY_HERE>",
) as s_client:

    res = s_client.batches.purchase(batch_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `batch_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Object ID of the batch                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[components.Batch](../../models/components/batch.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_shipments

Removes shipments from an existing batch shipment.

### Example Usage

<!-- UsageSnippet language="python" operationID="RemoveShipmentsFromBatch" method="post" path="/batches/{BatchId}/remove_shipments" -->
```python
from shippo import Shippo


with Shippo(
    shippo_api_version="2018-02-08",
    api_key_header="<YOUR_API_KEY_HERE>",
) as s_client:

    res = s_client.batches.remove_shipments(batch_id="<id>", request_body=[
        "<value 1>",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `batch_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Object ID of the batch                                              |
| `request_body`                                                      | List[*str*]                                                         | :heavy_check_mark:                                                  | Array of shipments object ids to remove from the batch              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[components.Batch](../../models/components/batch.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |