# Parcels
(*parcels*)

## Overview

A parcel is an item you are shipping. The parcel object includes details about its physical make-up of the parcel. It includes dimensions and weight that Shippo uses to calculate rates. 
<SchemaDefinition schemaRef="#/components/schemas/Parcel"/>

# Parcel Extras
The following values are supported for the `extra` field of the parcel object.
<SchemaDefinition schemaRef="#/components/schemas/ParcelExtra"/>

### Available Operations

* [list](#list) - List all parcels
* [create](#create) - Create a new parcel
* [get](#get) - Retrieve an existing parcel

## list

Returns a list of all parcel objects.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.parcels.list()

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

**[components.ParcelPaginatedList](../../models/components/parcelpaginatedlist.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |


## create

Creates a new parcel object.

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.parcels.create(request=components.ParcelCreateRequest(
    mass_unit=components.WeightUnitEnum.LB,
    weight='1',
    distance_unit=components.DistanceUnitEnum.IN,
    height='1',
    length='1',
    width='1',
    extra=components.ParcelExtra(
        cod=components.Cod(
            amount='5.5',
            currency='USD',
            payment_method=components.PaymentMethod.CASH,
        ),
        insurance=components.ParcelInsurance(
            amount='5.5',
            content='Laptop',
            currency='USD',
            provider=components.ParcelInsuranceProvider.UPS,
        ),
    ),
    metadata='Customer ID 123456',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateParcelRequestBody](../../models/operations/createparcelrequestbody.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |

### Response

**[components.Parcel](../../models/components/parcel.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |


## get

Returns parcel details using an existing parcel object ID (this will not return parcel details associated with un-purchased shipment/rate parcel object IDs).

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.parcels.get(parcel_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter               | Type                    | Required                | Description             |
| ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| `parcel_id`             | *str*                   | :heavy_check_mark:      | Object ID of the parcel |

### Response

**[components.Parcel](../../models/components/parcel.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
