# Pickups
(*pickups*)

## Overview

A pickup is when you schedule a carrier to collect a package for delivery.
Use Shippo’s pickups endpoint to schedule pickups with USPS and DHL Express for eligible shipments that you have already created.
<SchemaDefinition schemaRef="#/components/schemas/Pickup"/>

### Available Operations

* [create](#create) - Create a pickup

## create

Creates a pickup object. This request is for a carrier to come to a specified location to take a package for shipping.

### Example Usage

```python
import dateutil.parser
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.pickups.create(request=components.PickupBase(
    carrier_account='adcfdddf8ec64b84ad22772bce3ea37a',
    location=components.Location(
        address=components.AddressCompleteCreateRequest(
            name='Shwan Ippotle',
            street1='215 Clayton St.',
            city='San Francisco',
            state='CA',
            zip='94117',
            country='US',
            company='Shippo',
            street3='',
            street_no='',
            phone='+1 555 341 9393',
            email='shippotle@shippo.com',
            is_residential=True,
            metadata='Customer ID 123456',
            validate=True,
        ),
        building_location_type=components.BuildingLocationType.FRONT_DOOR,
        building_type=components.BuildingType.APARTMENT,
        instructions='Behind screen door',
    ),
    requested_end_time=dateutil.parser.isoparse('2023-06-18T07:14:55.338Z'),
    requested_start_time=dateutil.parser.isoparse('2023-12-01T17:06:07.804Z'),
    transactions=[
        'adcfdddf8ec64b84ad22772bce3ea37a',
    ],
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `request`                                                      | [components.PickupBase](../../models/components/pickupbase.md) | :heavy_check_mark:                                             | The request object to use for the request.                     |

### Response

**[components.Pickup](../../models/components/pickup.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |