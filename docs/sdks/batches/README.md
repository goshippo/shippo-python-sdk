# Batches
(*batches*)

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

* [create_batch](#create_batch) - Create a batch
* [get_batch](#get_batch) - Retrieve a batch
* [add_shipments_to_batch](#add_shipments_to_batch) - Add shipments to a batch
* [purchase_batch](#purchase_batch) - Purchase a batch
* [remove_shipments_from_batch](#remove_shipments_from_batch) - Remove shipments from a batch

## create_batch

Creates a new batch object for purchasing shipping labels for many shipments at once. Batches are created asynchronously. This means that the API response won't include your batch shipments yet. You need to retrieve the batch later to verify that all batch shipments are valid.

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.batches.create_batch(shippo_api_version='<value>', batch_create_request=components.BatchCreateRequest(
    default_carrier_account='078870331023437cb917f5187429b093',
    default_servicelevel_token='usps_priority',
    batch_shipments=[
        components.BatchShipmentBase(
            shipment=components.ShipmentCreateRequest(
                address_from='<value>',
                address_to='<value>',
                parcels=components.ParcelCreateRequest(
                    distance_unit=components.DistanceUnitTemplate.IN,
                    height='1',
                    length='1',
                    mass_unit=components.WeightUnit.LB,
                    weight='1',
                    width='1',
                    metadata='Customer ID 123456',
                ),
                customs_declaration='adcfdddf8ec64b84ad22772bce3ea37a',
                metadata='Customer ID 123456',
                shipment_date='2021-03-22T12:00:00Z',
                carrier_accounts=[
                    '065a4a8c10d24a34ab932163a1b87f52',
                    '73f706f4bdb94b54a337563840ce52b0',
                ],
            ),
            carrier_account='a4391cd4ab974f478f55dc08b5c8e3b3',
            metadata='SHIPMENT #1',
            servicelevel_token='fedex_ground',
        ),
    ],
    label_filetype=components.LabelFileType.PDF_4X6,
    metadata='BATCH #1',
))

if res.batch is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `shippo_api_version`                                                                     | *Optional[str]*                                                                          | :heavy_minus_sign:                                                                       | String used to pick a non-default API version to use                                     |
| `batch_create_request`                                                                   | [Optional[components.BatchCreateRequest]](../../models/components/batchcreaterequest.md) | :heavy_minus_sign:                                                                       | Batch details.                                                                           |


### Response

**[operations.CreateBatchResponse](../../models/operations/createbatchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_batch

Returns a batch using an object ID. <br> Batch shipments are displayed 100 at a time. You can iterate through each `page` using the `?page= query` parameter. You can also filter based on batch shipment status, for example, by passing a query param like `?object_results=creation_failed`. <br> For more details on filtering results,  see our guide on <a href="https://docs.goshippo.com/docs/api_concepts/filtering/" target="blank"> filtering</a>.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.batches.get_batch(batch_id='<value>', shippo_api_version='<value>')

if res.batch is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `batch_id`                                           | *str*                                                | :heavy_check_mark:                                   | Object ID of the batch                               |
| `shippo_api_version`                                 | *Optional[str]*                                      | :heavy_minus_sign:                                   | String used to pick a non-default API version to use |


### Response

**[operations.GetBatchResponse](../../models/operations/getbatchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## add_shipments_to_batch

Adds batch shipments to an existing batch.

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.batches.add_shipments_to_batch(batch_id='<value>', shippo_api_version='<value>', request_body=[
    components.BatchShipmentBase(
        shipment=components.ShipmentCreateRequest(
            address_from='<value>',
            address_to=components.AddressCreateRequest(
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
            parcels=components.ParcelCreateRequest(
                distance_unit=components.DistanceUnitTemplate.IN,
                height='1',
                length='1',
                mass_unit=components.WeightUnit.LB,
                weight='1',
                width='1',
                metadata='Customer ID 123456',
            ),
            customs_declaration='adcfdddf8ec64b84ad22772bce3ea37a',
            metadata='Customer ID 123456',
            shipment_date='2021-03-22T12:00:00Z',
            carrier_accounts=[
                '065a4a8c10d24a34ab932163a1b87f52',
                '73f706f4bdb94b54a337563840ce52b0',
            ],
        ),
        carrier_account='a4391cd4ab974f478f55dc08b5c8e3b3',
        metadata='SHIPMENT #1',
        servicelevel_token='fedex_ground',
    ),
])

if res.batch is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `batch_id`                                                                         | *str*                                                                              | :heavy_check_mark:                                                                 | Object ID of the batch                                                             |
| `shippo_api_version`                                                               | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | String used to pick a non-default API version to use                               |
| `request_body`                                                                     | List[[components.BatchShipmentBase](../../models/components/batchshipmentbase.md)] | :heavy_minus_sign:                                                                 | Array of shipments to add to the batch                                             |


### Response

**[operations.AddShipmentsToBatchResponse](../../models/operations/addshipmentstobatchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## purchase_batch

Purchases an existing batch with a status of `VALID`. 
Once you send a POST request to the purchase endpoint the batch status will change to `PURCHASING`. 
When all the shipments are purchased, the status will change to `PURCHASED` and you will receive a 
`batch_purchased` webhook indicating that the batch has been purchased

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.batches.purchase_batch(batch_id='<value>', shippo_api_version='<value>')

if res.batch is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `batch_id`                                           | *str*                                                | :heavy_check_mark:                                   | Object ID of the batch                               |
| `shippo_api_version`                                 | *Optional[str]*                                      | :heavy_minus_sign:                                   | String used to pick a non-default API version to use |


### Response

**[operations.PurchaseBatchResponse](../../models/operations/purchasebatchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_shipments_from_batch

Removes shipments from an existing batch shipment.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.batches.remove_shipments_from_batch(batch_id='<value>', shippo_api_version='<value>', request_body=[
    '<value>',
])

if res.batch is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                              | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `batch_id`                                             | *str*                                                  | :heavy_check_mark:                                     | Object ID of the batch                                 |
| `shippo_api_version`                                   | *Optional[str]*                                        | :heavy_minus_sign:                                     | String used to pick a non-default API version to use   |
| `request_body`                                         | List[*str*]                                            | :heavy_minus_sign:                                     | Array of shipments object ids to remove from the batch |


### Response

**[operations.RemoveShipmentsFromBatchResponse](../../models/operations/removeshipmentsfrombatchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
