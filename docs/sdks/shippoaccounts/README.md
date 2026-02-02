# ShippoAccounts

## Overview

Shippo Accounts are used by Shippo Platform Accounts to create and manage Managed Shippo Accounts. 
Managed Shippo Accounts are headless accounts that represent your customers. They are opaque to your end customers, meaning customers do not need to create their own Shippo login or have a billing relationship with Shippo. 
They can be used by marketplaces, e-commerce platforms, and third-party logistics providers who want to offer, seamless, built-in shipping functionality to their customers. See our <a href="https://docs.goshippo.com/docs/platformaccounts/platform_accounts/">guide</a> for more details.
<SchemaDefinition schemaRef="#/components/schemas/ShippoAccount"/>

### Available Operations

* [list](#list) - List all Shippo Accounts
* [create](#create) - Create a Shippo Account
* [get](#get) - Retrieve a Shippo Account
* [update](#update) - Update a Shippo Account

## list

Returns a list of Shippo Managed Accounts objects.

### Example Usage

<!-- UsageSnippet language="python" operationID="ListShippoAccounts" method="get" path="/shippo-accounts" -->
```python
from shippo import Shippo


with Shippo(
    shippo_api_version="2018-02-08",
    api_key_header="<YOUR_API_KEY_HERE>",
) as s_client:

    res = s_client.shippo_accounts.list(page=1, results=25)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The page number you want to select                                  |
| `results`                                                           | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The number of results to return per page (max 100)                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[components.ShippoAccountPaginatedList](../../models/components/shippoaccountpaginatedlist.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create

Creates a new <a href="https://docs.goshippo.com/docs/platformaccounts/platform_using_accounts/">Shippo Managed Account</a>.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateShippoAccount" method="post" path="/shippo-accounts" -->
```python
from shippo import Shippo


with Shippo(
    shippo_api_version="2018-02-08",
    api_key_header="<YOUR_API_KEY_HERE>",
) as s_client:

    res = s_client.shippo_accounts.create(request={
        "email": "hippo@shippo.com",
        "first_name": "Shippo",
        "last_name": "Meister",
        "company_name": "Acme",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [components.ShippoAccountUpdateRequest](../../models/components/shippoaccountupdaterequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[components.ShippoAccount](../../models/components/shippoaccount.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get

Returns a Shippo Managed Account using an object ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetShippoAccount" method="get" path="/shippo-accounts/{ShippoAccountId}" -->
```python
from shippo import Shippo


with Shippo(
    shippo_api_version="2018-02-08",
    api_key_header="<YOUR_API_KEY_HERE>",
) as s_client:

    res = s_client.shippo_accounts.get(shippo_account_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `shippo_account_id`                                                 | *str*                                                               | :heavy_check_mark:                                                  | Object ID of the ShippoAccount                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[components.ShippoAccount](../../models/components/shippoaccount.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update

Updates a Shippo Managed Account using an object ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateShippoAccount" method="put" path="/shippo-accounts/{ShippoAccountId}" -->
```python
from shippo import Shippo


with Shippo(
    shippo_api_version="2018-02-08",
    api_key_header="<YOUR_API_KEY_HERE>",
) as s_client:

    res = s_client.shippo_accounts.update(shippo_account_id="<id>", shippo_account_update_request={
        "email": "hippo@shippo.com",
        "first_name": "Shippo",
        "last_name": "Meister",
        "company_name": "Acme",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `shippo_account_id`                                                                                      | *str*                                                                                                    | :heavy_check_mark:                                                                                       | Object ID of the ShippoAccount                                                                           |
| `shippo_account_update_request`                                                                          | [Optional[components.ShippoAccountUpdateRequest]](../../models/components/shippoaccountupdaterequest.md) | :heavy_minus_sign:                                                                                       | N/A                                                                                                      |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[components.ShippoAccount](../../models/components/shippoaccount.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |