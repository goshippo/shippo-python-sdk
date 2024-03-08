# Shipments
(*shipments*)

## Overview

A shipment is the act of transporting goods. A shipment object contains **to** and **from** addresses, and the parcel details that you are shipping. You can use the shipment object to retrieve shipping rates and purchase a shipping label.
<SchemaDefinition schemaRef="#/components/schemas/Shipment"/>
 
# Shipment Extras
The following values are supported for the `extra` field of the shipment object.
<SchemaDefinition schemaRef="#/components/schemas/ShipmentExtra"/>

### Available Operations

* [list_shipments](#list_shipments) - List all shipments
* [create_shipment](#create_shipment) - Create a new shipment
* [get_shipment](#get_shipment) - Retrieve a shipment

## list_shipments

Returns a list of all shipment objects.<br><br>
In order to filter results, you must use the below path parameters. 
A maximum date range of 90 days is permitted. 
Provided dates should be ISO 8601 UTC dates (timezone offsets are currently not supported).<br><br>

Optional path parameters:<br>
  `object_created_gt`- object(s) created greater than a provided date time<br>
  `object_created_gte` - object(s) created greater than or equal to a provided date time<br>
  `object_created_lt` - object(s) created less than a provided date time<br>
  `object_created_lte` - object(s) created less than or equal to a provided date time<br>

  Date format examples:<br>
    `2017-01-01`<br>
    `2017-01-01T03:30:30` or `2017-01-01T03:30:30.5`<br>
    `2017-01-01T03:30:30Z`<br><br>

  Example URL:<br>
    `https://api.goshippo.com/shipments/?object_created_gte=2017-01-01T00:00:30&object_created_lt=2017-04-01T00:00:30`

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.shipments.list_shipments(page=1, results=25, shippo_api_version='<value>')

if res.shipment_list_wrapper is not None:
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

**[operations.ListShipmentsResponse](../../models/operations/listshipmentsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_shipment

Creates a new shipment object.

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.shipments.create_shipment(shippo_api_version='<value>', shipment_create_request=components.ShipmentCreateRequest(
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
    parcels=[
        components.ParcelCreateRequest(
            distance_unit=components.DistanceUnitTemplate.IN,
            height='1',
            length='1',
            mass_unit=components.WeightUnit.LB,
            weight='1',
            width='1',
            metadata='Customer ID 123456',
        ),
    ],
    customs_declaration='adcfdddf8ec64b84ad22772bce3ea37a',
    metadata='Customer ID 123456',
    shipment_date='2021-03-22T12:00:00Z',
))

if res.shipment is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `shippo_api_version`                                                                           | *Optional[str]*                                                                                | :heavy_minus_sign:                                                                             | String used to pick a non-default API version to use                                           |
| `shipment_create_request`                                                                      | [Optional[components.ShipmentCreateRequest]](../../models/components/shipmentcreaterequest.md) | :heavy_minus_sign:                                                                             | Shipment details and contact info.                                                             |


### Response

**[operations.CreateShipmentResponse](../../models/operations/createshipmentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_shipment

Returns an existing shipment using an object ID

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.shipments.get_shipment(shipment_id='<value>', shippo_api_version='<value>')

if res.shipment is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `shipment_id`                                        | *str*                                                | :heavy_check_mark:                                   | Object ID of the shipment to update                  |
| `shippo_api_version`                                 | *Optional[str]*                                      | :heavy_minus_sign:                                   | String used to pick a non-default API version to use |


### Response

**[operations.GetShipmentResponse](../../models/operations/getshipmentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
