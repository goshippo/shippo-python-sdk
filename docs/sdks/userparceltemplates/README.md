# UserParcelTemplates

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

<!-- UsageSnippet language="python" operationID="ListUserParcelTemplates" method="get" path="/user-parcel-templates" -->
```python
from shippo import Shippo


with Shippo(
    shippo_api_version="2018-02-08",
    api_key_header="<YOUR_API_KEY_HERE>",
) as s_client:

    res = s_client.user_parcel_templates.list(request={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListUserParcelTemplatesRequest](../../models/operations/listuserparceltemplatesrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

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

<!-- UsageSnippet language="python" operationID="CreateUserParcelTemplate" method="post" path="/user-parcel-templates" -->
```python
from shippo import Shippo
from shippo.models import components


with Shippo(
    shippo_api_version="2018-02-08",
    api_key_header="<YOUR_API_KEY_HERE>",
) as s_client:

    res = s_client.user_parcel_templates.create(request={
        "distance_unit": components.DistanceUnitEnum.IN,
        "height": "6",
        "length": "10",
        "name": "My Custom Template",
        "weight": "12",
        "weight_unit": components.WeightUnitEnum.LB,
        "width": "8",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [components.UserParcelTemplateCreateRequest](../../models/components/userparceltemplatecreaterequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[components.UserParcelTemplate](../../models/components/userparceltemplate.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete

Deletes a user parcel template using an object ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteUserParcelTemplate" method="delete" path="/user-parcel-templates/{UserParcelTemplateObjectId}" -->
```python
from shippo import Shippo


with Shippo(
    shippo_api_version="2018-02-08",
    api_key_header="<YOUR_API_KEY_HERE>",
) as s_client:

    s_client.user_parcel_templates.delete(user_parcel_template_object_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_parcel_template_object_id`                                    | *str*                                                               | :heavy_check_mark:                                                  | Object ID of the user parcel template                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get

Returns the parcel template information for a specific user parcel
template, identified by the object ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetUserParcelTemplate" method="get" path="/user-parcel-templates/{UserParcelTemplateObjectId}" -->
```python
from shippo import Shippo


with Shippo(
    shippo_api_version="2018-02-08",
    api_key_header="<YOUR_API_KEY_HERE>",
) as s_client:

    res = s_client.user_parcel_templates.get(user_parcel_template_object_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_parcel_template_object_id`                                    | *str*                                                               | :heavy_check_mark:                                                  | Object ID of the user parcel template                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[components.UserParcelTemplate](../../models/components/userparceltemplate.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update

Updates an existing user parcel template.

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateUserParcelTemplate" method="put" path="/user-parcel-templates/{UserParcelTemplateObjectId}" -->
```python
from shippo import Shippo
from shippo.models import components


with Shippo(
    shippo_api_version="2018-02-08",
    api_key_header="<YOUR_API_KEY_HERE>",
) as s_client:

    res = s_client.user_parcel_templates.update(user_parcel_template_object_id="<id>", user_parcel_template_update_request={
        "distance_unit": components.DistanceUnitEnum.IN,
        "height": "6",
        "length": "10",
        "name": "My Custom Template",
        "weight": "12",
        "weight_unit": components.WeightUnitEnum.LB,
        "width": "8",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `user_parcel_template_object_id`                                                                                   | *str*                                                                                                              | :heavy_check_mark:                                                                                                 | Object ID of the user parcel template                                                                              |
| `user_parcel_template_update_request`                                                                              | [Optional[components.UserParcelTemplateUpdateRequest]](../../models/components/userparceltemplateupdaterequest.md) | :heavy_minus_sign:                                                                                                 | N/A                                                                                                                |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[components.UserParcelTemplate](../../models/components/userparceltemplate.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |