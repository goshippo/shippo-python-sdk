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

* [list](#list) - List all user parcel templates
* [create](#create) - Create a new user parcel template
* [delete](#delete) - Delete a user parcel template
* [get](#get) - Retrieves a user parcel template
* [update](#update) - Update an existing user parcel template

## list

Returns a list all of all user parcel template objects.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.user_parcel_templates.list()

if res is not None:
    # handle response
    pass

```

### Response

**[components.UserParcelTemplateList](../../models/components/userparceltemplatelist.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create

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
    shippo_api_version='2018-02-08',
)


res = s.user_parcel_templates.create(request=components.UserParcelTemplateWithCarrierTemplateCreateRequest(
    weight='12',
    weight_unit=components.WeightUnitEnum.LB,
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [components.UserParcelTemplateCreateRequest](../../models/components/userparceltemplatecreaterequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |

### Response

**[components.UserParcelTemplate](../../models/components/userparceltemplate.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete

Deletes a user parcel template using an object ID.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


s.user_parcel_templates.delete(user_parcel_template_object_id='<value>')

# Use the SDK ...

```

### Parameters

| Parameter                             | Type                                  | Required                              | Description                           |
| ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| `user_parcel_template_object_id`      | *str*                                 | :heavy_check_mark:                    | Object ID of the user parcel template |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get

Returns the parcel template information for a specific user parcel
template, identified by the object ID.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.user_parcel_templates.get(user_parcel_template_object_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                             | Type                                  | Required                              | Description                           |
| ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| `user_parcel_template_object_id`      | *str*                                 | :heavy_check_mark:                    | Object ID of the user parcel template |

### Response

**[components.UserParcelTemplate](../../models/components/userparceltemplate.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update

Updates an existing user parcel template.

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.user_parcel_templates.update(user_parcel_template_object_id='<value>', user_parcel_template_update_request=components.UserParcelTemplateUpdateRequest(
    distance_unit=components.DistanceUnitEnum.IN,
    height='6',
    length='10',
    name='My Custom Template',
    width='8',
    weight='12',
    weight_unit=components.WeightUnitEnum.LB,
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `user_parcel_template_object_id`                                                                                   | *str*                                                                                                              | :heavy_check_mark:                                                                                                 | Object ID of the user parcel template                                                                              |
| `user_parcel_template_update_request`                                                                              | [Optional[components.UserParcelTemplateUpdateRequest]](../../models/components/userparceltemplateupdaterequest.md) | :heavy_minus_sign:                                                                                                 | N/A                                                                                                                |

### Response

**[components.UserParcelTemplate](../../models/components/userparceltemplate.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |