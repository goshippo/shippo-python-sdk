# Parcels
(*parcels*)

## Overview

A parcel is an item you are shipping. The parcel object includes details about its physical make-up of the parcel. It includes dimensions and weight that Shippo uses to calculate rates. 
<SchemaDefinition schemaRef="#/components/schemas/Parcel"/>

# Parcel Extras
The following values are supported for the `extra` field of the parcel object.
<SchemaDefinition schemaRef="#/components/schemas/ParcelExtra"/>

### Available Operations

* [list_parcels](#list_parcels) - List all parcels
* [create_parcel](#create_parcel) - Create a new parcel
* [get_parcel](#get_parcel) - Retrieve an existing parcel

## list_parcels

Returns a list of all parcel objects.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.parcels.list_parcels(page=1, results=25, shippo_api_version='<value>')

if res.parcel_list_wrapper is not None:
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

**[operations.ListParcelsResponse](../../models/operations/listparcelsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_parcel

Creates a new parcel object.

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.parcels.create_parcel(shippo_api_version='<value>', parcel_request=components.ParcelRequest(
    distance_unit=components.DistanceUnitTemplate.IN,
    height='1',
    length='1',
    mass_unit=components.WeightUnit.LB,
    weight='1',
    width='1',
))

if res.parcel is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `shippo_api_version`                                                           | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | String used to pick a non-default API version to use                           |
| `parcel_request`                                                               | [Optional[components.ParcelRequest]](../../models/components/parcelrequest.md) | :heavy_minus_sign:                                                             | Parcel details.                                                                |


### Response

**[operations.CreateParcelResponse](../../models/operations/createparcelresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_parcel

Returns parcel details using an existing parcel object ID (this will not return parcel details associated with un-purchased shipment/rate parcel object IDs).

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.parcels.get_parcel(parcel_id='<value>', shippo_api_version='<value>')

if res.parcel is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `parcel_id`                                          | *str*                                                | :heavy_check_mark:                                   | Object ID of the parcel                              |
| `shippo_api_version`                                 | *Optional[str]*                                      | :heavy_minus_sign:                                   | String used to pick a non-default API version to use |


### Response

**[operations.GetParcelResponse](../../models/operations/getparcelresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
