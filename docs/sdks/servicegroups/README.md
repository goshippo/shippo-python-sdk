# ServiceGroups
(*service_groups*)

## Overview

A service group is a set of service levels grouped together. 
Rates at checkout uses services groups to present available shipping options to customers in their shopping basket.
<SchemaDefinition schemaRef="#/components/schemas/ServiceGroup"/>

### Available Operations

* [list](#list) - List all service groups
* [create](#create) - Create a new service group
* [update](#update) - Update an existing service group
* [delete](#delete) - Delete a service group

## list

Returns a list of service group objects.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.service_groups.list()

if res is not None:
    # handle response
    pass

```

### Response

**[List[components.ServiceGroup]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create

Creates a new service group.

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.service_groups.create(request=components.ServiceGroupCreateRequest(
    description='USPS shipping options',
    name='USPS Shipping',
    type=components.ServiceGroupTypeEnum.FLAT_RATE,
    service_levels=[
        components.ServiceGroupAccountAndServiceLevel(
            account_object_id='80feb1633d4a43c898f0058506cfd82d',
            service_level_token='ups_next_day_air_saver',
        ),
    ],
    flat_rate='5',
    flat_rate_currency='USD',
    free_shipping_threshold_currency='USD',
    free_shipping_threshold_min='5',
    rate_adjustment=15,
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [components.ServiceGroupCreateRequest](../../models/components/servicegroupcreaterequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |

### Response

**[components.ServiceGroup](../../models/components/servicegroup.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update

Updates an existing service group object. <br>The object_id cannot be updated as it is the unique identifier for the object.

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.service_groups.update(request=components.ServiceGroupUpdateRequest(
    description='USPS shipping options',
    name='USPS Shipping',
    type=components.ServiceGroupTypeEnum.FLAT_RATE,
    object_id='80feb1633d4a43c898f005850',
    is_active=True,
    service_levels=[
        components.ServiceGroupAccountAndServiceLevel(
            account_object_id='80feb1633d4a43c898f0058506cfd82d',
            service_level_token='ups_next_day_air_saver',
        ),
        components.ServiceGroupAccountAndServiceLevel(
            account_object_id='80feb1633d4a43c898f0058506cfd82d',
            service_level_token='ups_next_day_air_saver',
        ),
        components.ServiceGroupAccountAndServiceLevel(
            account_object_id='80feb1633d4a43c898f0058506cfd82d',
            service_level_token='ups_next_day_air_saver',
        ),
    ],
    flat_rate='5',
    flat_rate_currency='USD',
    free_shipping_threshold_currency='USD',
    free_shipping_threshold_min='5',
    rate_adjustment=15,
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [components.ServiceGroupUpdateRequest](../../models/components/servicegroupupdaterequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |

### Response

**[components.ServiceGroup](../../models/components/servicegroup.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete

Deletes an existing service group using an object ID.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


s.service_groups.delete(service_group_id='<value>')

# Use the SDK ...

```

### Parameters

| Parameter                      | Type                           | Required                       | Description                    |
| ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ |
| `service_group_id`             | *str*                          | :heavy_check_mark:             | Object ID of the service group |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |