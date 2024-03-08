# ServiceGroups
(*service_groups*)

## Overview

A service group is a set of service levels grouped together. 
Rates at checkout uses services groups to present available shipping options to customers in their shopping basket.
<SchemaDefinition schemaRef="#/components/schemas/ServiceGroup"/>

### Available Operations

* [list_service_groups](#list_service_groups) - List all service groups
* [create_service_group](#create_service_group) - Create a new service group
* [update_service_group](#update_service_group) - Update an existing service group
* [delete_service_group](#delete_service_group) - Delete a service group

## list_service_groups

Returns a list of service group objects.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.service_groups.list_service_groups(shippo_api_version='<value>')

if res.service_group_list_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `shippo_api_version`                                 | *Optional[str]*                                      | :heavy_minus_sign:                                   | String used to pick a non-default API version to use |


### Response

**[operations.ListServiceGroupsResponse](../../models/operations/listservicegroupsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_service_group

Creates a new service group.

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.service_groups.create_service_group(shippo_api_version='<value>', service_group_create_request=components.ServiceGroupCreateRequest(
    description='USPS shipping options',
    name='USPS Shipping',
    service_levels=[
        components.ServiceLevel(
            name='Priority Mail Express',
            service_level_token='usps_priority_express',
        ),
    ],
    type=components.ServiceGroupCreateRequestType.FLAT_RATE,
    flat_rate='5',
    flat_rate_currency='USD',
    free_shipping_threshold_currency='USD',
    free_shipping_threshold_min='5',
    rate_adjustment=15,
))

if res.service_group is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `shippo_api_version`                                                                                   | *Optional[str]*                                                                                        | :heavy_minus_sign:                                                                                     | String used to pick a non-default API version to use                                                   |
| `service_group_create_request`                                                                         | [Optional[components.ServiceGroupCreateRequest]](../../models/components/servicegroupcreaterequest.md) | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |


### Response

**[operations.CreateServiceGroupResponse](../../models/operations/createservicegroupresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_service_group

Updates an existing service group object. <br>The object_id cannot be updated as it is the unique identifier for the object.

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.service_groups.update_service_group(shippo_api_version='<value>', service_group=components.ServiceGroup(
    description='USPS shipping options',
    name='USPS Shipping',
    service_levels=[
        components.ServiceLevel(
            name='Priority Mail Express',
            service_level_token='usps_priority_express',
        ),
    ],
    type=components.ServiceGroupType.FLAT_RATE,
    object_id='80feb1633d4a43c898f005850',
    flat_rate='5',
    flat_rate_currency='USD',
    free_shipping_threshold_currency='USD',
    free_shipping_threshold_min='5',
    rate_adjustment=15,
    is_active=True,
))

if res.service_group is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `shippo_api_version`                                                         | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | String used to pick a non-default API version to use                         |
| `service_group`                                                              | [Optional[components.ServiceGroup]](../../models/components/servicegroup.md) | :heavy_minus_sign:                                                           | N/A                                                                          |


### Response

**[operations.UpdateServiceGroupResponse](../../models/operations/updateservicegroupresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_service_group

Deletes an existing service group using an object ID.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.service_groups.delete_service_group(service_group_id='<value>', shippo_api_version='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `service_group_id`                                   | *str*                                                | :heavy_check_mark:                                   | Object ID of the service group                       |
| `shippo_api_version`                                 | *Optional[str]*                                      | :heavy_minus_sign:                                   | String used to pick a non-default API version to use |


### Response

**[operations.DeleteServiceGroupResponse](../../models/operations/deleteservicegroupresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
