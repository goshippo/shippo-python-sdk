# RatesAtCheckout

## Overview

Rates at checkout is a tool for merchants to display up-to-date shipping estimates based on what's in their customers cart and where they’re shipping to.
Merchants set up curated shipping options for customers in the checkout flow based on data in the shopping cart. The request must include the **to** address and item information. Optional fields are the **from** address and package information. If the optional fields are not included, the service will use the default address and/or package configured for rates at checkout. The response is a list of shipping options based on the Service Group configuration.
(see <a href="#tag/Service-Groups">Service Group configuration</a> for details).
<SchemaDefinition schemaRef="#/components/schemas/LiveRate"/>


# Default Parcel Template
Assign one of your user parcel templates to be the default used when generating Live Rates. This template will be used by default when generating Live Rates, unless you explicitly provide a parcel in the Live Rates request.
<SchemaDefinition schemaRef="#/components/schemas/UserParcelTemplate"/>

### Available Operations

* [create](#create) - Generate a live rates request
* [get_default_parcel_template](#get_default_parcel_template) - Show current default parcel template
* [update_default_parcel_template](#update_default_parcel_template) - Update default parcel template
* [delete_default_parcel_template](#delete_default_parcel_template) - Clear current default parcel template

## create

Initiates a live rates request. Include either the object ID for
an existing address record or a fully formed address object when entering
an address value. You can also enter the object ID of an existing user parcel
template or a fully formed user parcel template object as the parcel value.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateLiveRate" method="post" path="/live-rates" -->
```python
from shippo import Shippo
from shippo.models import components


with Shippo(
    shippo_api_version="2018-02-08",
    api_key_header="<YOUR_API_KEY_HERE>",
) as s_client:

    res = s_client.rates_at_checkout.create(request=components.LiveRateCreateRequest(
        address_from="<value>",
        address_to="<value>",
        line_items=[],
        parcel="5df144dca289442cv7a06",
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [components.LiveRateCreateRequest](../../models/components/liveratecreaterequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[components.LiveRatePaginatedList](../../models/components/liveratepaginatedlist.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_default_parcel_template

Retrieve and display the currently configured default parcel template for live rates.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetDefaultParcelTemplate" method="get" path="/live-rates/settings/parcel-template" -->
```python
from shippo import Shippo


with Shippo(
    shippo_api_version="2018-02-08",
    api_key_header="<YOUR_API_KEY_HERE>",
) as s_client:

    res = s_client.rates_at_checkout.get_default_parcel_template(request={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetDefaultParcelTemplateRequest](../../models/operations/getdefaultparceltemplaterequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[components.DefaultParcelTemplate](../../models/components/defaultparceltemplate.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_default_parcel_template

Update the currently configured default parcel template for live rates. The object_id in the request payload should identify the user parcel template to be the new default.

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateDefaultParcelTemplate" method="put" path="/live-rates/settings/parcel-template" -->
```python
from shippo import Shippo


with Shippo(
    shippo_api_version="2018-02-08",
    api_key_header="<YOUR_API_KEY_HERE>",
) as s_client:

    res = s_client.rates_at_checkout.update_default_parcel_template(request={
        "object_id": "b958d3690bb04bb8b2986724872750f5",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [components.DefaultParcelTemplateUpdateRequest](../../models/components/defaultparceltemplateupdaterequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[components.DefaultParcelTemplate](../../models/components/defaultparceltemplate.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_default_parcel_template

Clears the currently configured default parcel template for live rates.

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteDefaultParcelTemplate" method="delete" path="/live-rates/settings/parcel-template" -->
```python
from shippo import Shippo


with Shippo(
    shippo_api_version="2018-02-08",
    api_key_header="<YOUR_API_KEY_HERE>",
) as s_client:

    s_client.rates_at_checkout.delete_default_parcel_template(request={})

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.DeleteDefaultParcelTemplateRequest](../../models/operations/deletedefaultparceltemplaterequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |