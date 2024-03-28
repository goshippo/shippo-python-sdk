# Manifests
(*manifests*)

## Overview

A manifest is a single-page document with a barcode that carriers can scan to accept all packages into transit without the need to scan each item individually. 
They are close-outs of shipping labels of a certain day. Some carriers require manifests to  process the shipments.

<SchemaDefinition schemaRef="#/components/schemas/Manifest"/>

# Manifest Errors
The following codes and messages are the possible errors that may occur when creating Manifests.
<SchemaDefinition schemaRef="#/components/schemas/ManifestErrors"/>

### Available Operations

* [list_manifests](#list_manifests) - List all manifests
* [create_manifest](#create_manifest) - Create a new manifest
* [get_manifest](#get_manifest) - Retrieve a manifest

## list_manifests

Returns a list of all manifest objects.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.manifests.list_manifests(page=1, results=25, shippo_api_version='<value>')

if res.manifest_paginated_list is not None:
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

**[operations.ListManifestsResponse](../../models/operations/listmanifestsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_manifest

Creates a new manifest object.

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.manifests.create_manifest(shippo_api_version='<value>', manifest_create_request=components.ManifestCreateRequest(
    carrier_account='adcfdddf8ec64b84ad22772bce3ea37a',
    shipment_date='2014-05-16T23:59:59Z',
    address_from=components.AddressCreateRequest(
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
    transactions=[
        'adcfdddf8ec64b84ad22772bce3ea37a',
    ],
))

if res.manifest is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `shippo_api_version`                                                                           | *Optional[str]*                                                                                | :heavy_minus_sign:                                                                             | String used to pick a non-default API version to use                                           |
| `manifest_create_request`                                                                      | [Optional[components.ManifestCreateRequest]](../../models/components/manifestcreaterequest.md) | :heavy_minus_sign:                                                                             | Manifest details and contact info.                                                             |


### Response

**[operations.CreateManifestResponse](../../models/operations/createmanifestresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_manifest

Returns an existing manifest using an object ID.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.manifests.get_manifest(manifest_id='<value>', shippo_api_version='<value>')

if res.manifest is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `manifest_id`                                        | *str*                                                | :heavy_check_mark:                                   | Object ID of the manifest to update                  |
| `shippo_api_version`                                 | *Optional[str]*                                      | :heavy_minus_sign:                                   | String used to pick a non-default API version to use |


### Response

**[operations.GetManifestResponse](../../models/operations/getmanifestresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
