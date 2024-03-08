# UserParcelTemplates
(*user_parcel_templates*)

## Overview

A user parcel template represents a package used for shipping that has preset dimensions and attributes defined 
by you. They are useful for capturing attributes of parcel-types you frequently use for shipping, allowing 
them to be defined once and then used for many shipments. These parcel templates can also be used for live rates.

User parcel templates can also be created using a carrier parcel template, where the dimensions will be copied from 
the carrier presets, but the weight can be configured by you.
<SchemaDefinition schemaRef="#/components/schemas/UserParcelTemplate"/>

### Available Operations

* [list_user_parcel_templates](#list_user_parcel_templates) - List all user parcel templates
* [create_user_parcel_template](#create_user_parcel_template) - Create a new user parcel template
* [delete_user_parcel_template](#delete_user_parcel_template) - Delete a user parcel template
* [get_user_parcel_template](#get_user_parcel_template) - Retrieves a user parcel template
* [update_user_parcel_template](#update_user_parcel_template) - Update an existing user parcel template

## list_user_parcel_templates

Returns a list all of all user parcel template objects.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.user_parcel_templates.list_user_parcel_templates(shippo_api_version='<value>')

if res.user_parcel_template_list is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `shippo_api_version`                                 | *Optional[str]*                                      | :heavy_minus_sign:                                   | String used to pick a non-default API version to use |


### Response

**[operations.ListUserParcelTemplatesResponse](../../models/operations/listuserparceltemplatesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_user_parcel_template

Creates a new user parcel template. <br>You can choose to create a
parcel template using a preset carrier template as a starting point, or
you can create an entirely custom one. To use a preset carrier template,
pass in a unique template token from <a href="#tag/Parcel-Templates">this list</a>
plus the weight fields (**weight** and **weight_unit**). Otherwise, omit
the template field and pass the other fields, for the weight, length, height,
and depth, as well as their units."

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.user_parcel_templates.create_user_parcel_template(shippo_api_version='<value>', user_parcel_template_create_request=components.UserParcelTemplateWithoutCarrierTemplateCreateRequest(
    distance_unit=components.DistanceUnitUserTemplate.IN,
    height='6',
    length='10',
    name='My Custom Template',
    width='8',
    weight='12',
    weight_unit=components.WeightUnit.LB,
))

if res.user_parcel_template is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                      | Type                                                                                                                                                                                                           | Required                                                                                                                                                                                                       | Description                                                                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `shippo_api_version`                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                             | String used to pick a non-default API version to use                                                                                                                                                           |
| `user_parcel_template_create_request`                                                                                                                                                                          | [Optional[Union[components.UserParcelTemplateWithCarrierTemplateCreateRequest, components.UserParcelTemplateWithoutCarrierTemplateCreateRequest]]](../../models/components/userparceltemplatecreaterequest.md) | :heavy_minus_sign:                                                                                                                                                                                             | N/A                                                                                                                                                                                                            |


### Response

**[operations.CreateUserParcelTemplateResponse](../../models/operations/createuserparceltemplateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_user_parcel_template

Deletes a user parcel template using an object ID.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.user_parcel_templates.delete_user_parcel_template(user_parcel_template_object_id='<value>', shippo_api_version='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `user_parcel_template_object_id`                     | *str*                                                | :heavy_check_mark:                                   | Object ID of the user parcel template                |
| `shippo_api_version`                                 | *Optional[str]*                                      | :heavy_minus_sign:                                   | String used to pick a non-default API version to use |


### Response

**[operations.DeleteUserParcelTemplateResponse](../../models/operations/deleteuserparceltemplateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_user_parcel_template

Returns the parcel template information for a specific user parcel
template, identified by the object ID.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.user_parcel_templates.get_user_parcel_template(user_parcel_template_object_id='<value>', shippo_api_version='<value>')

if res.user_parcel_template is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `user_parcel_template_object_id`                     | *str*                                                | :heavy_check_mark:                                   | Object ID of the user parcel template                |
| `shippo_api_version`                                 | *Optional[str]*                                      | :heavy_minus_sign:                                   | String used to pick a non-default API version to use |


### Response

**[operations.GetUserParcelTemplateResponse](../../models/operations/getuserparceltemplateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_user_parcel_template

Updates an existing user parcel template.

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.user_parcel_templates.update_user_parcel_template(user_parcel_template_object_id='<value>', shippo_api_version='<value>', user_parcel_template_update_request=components.UserParcelTemplateUpdateRequest(
    distance_unit=components.DistanceUnitUserTemplate.IN,
    height='6',
    length='10',
    name='My Custom Template',
    width='8',
    weight='12',
    weight_unit=components.WeightUnit.LB,
))

if res.user_parcel_template is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `user_parcel_template_object_id`                                                                                   | *str*                                                                                                              | :heavy_check_mark:                                                                                                 | Object ID of the user parcel template                                                                              |
| `shippo_api_version`                                                                                               | *Optional[str]*                                                                                                    | :heavy_minus_sign:                                                                                                 | String used to pick a non-default API version to use                                                               |
| `user_parcel_template_update_request`                                                                              | [Optional[components.UserParcelTemplateUpdateRequest]](../../models/components/userparceltemplateupdaterequest.md) | :heavy_minus_sign:                                                                                                 | N/A                                                                                                                |


### Response

**[operations.UpdateUserParcelTemplateResponse](../../models/operations/updateuserparceltemplateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
