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
)


res = s.parcels.list(page=1, results=25, shippo_api_version='<value>')

if res is not None:
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

**[components.ParcelPaginatedList](../../models/components/parcelpaginatedlist.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create

Creates a new parcel object.

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.parcels.create(shippo_api_version='<value>', parcel_request=components.ParcelRequest(
    distance_unit=components.DistanceUnitTemplate.IN,
    height='1',
    length='1',
    mass_unit=components.WeightUnit.LB,
    weight='1',
    width='1',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `shippo_api_version`                                                           | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | String used to pick a non-default API version to use                           |
| `parcel_request`                                                               | [Optional[components.ParcelRequest]](../../models/components/parcelrequest.md) | :heavy_minus_sign:                                                             | Parcel details.                                                                |


### Response

**[components.Parcel](../../models/components/parcel.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get

Returns parcel details using an existing parcel object ID (this will not return parcel details associated with un-purchased shipment/rate parcel object IDs).

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.parcels.get(parcel_id='<value>', shippo_api_version='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `parcel_id`                                          | *str*                                                | :heavy_check_mark:                                   | Object ID of the parcel                              |
| `shippo_api_version`                                 | *Optional[str]*                                      | :heavy_minus_sign:                                   | String used to pick a non-default API version to use |


### Response

**[components.Parcel](../../models/components/parcel.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
