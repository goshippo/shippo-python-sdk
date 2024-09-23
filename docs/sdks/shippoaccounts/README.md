# ShippoAccounts
(*shippo_accounts*)

## Overview

Shippo Accounts are used by Shippo Platform Accounts to create and manage Managed Shippo Accounts. 
Managed Shippo Accounts are headless accounts that represent your customers. They are opaque to your end customers, meaning customers do not need to create their own Shippo login or have a billing relationship with Shippo. 
They can be used by marketplaces, e-commerce platforms, and third-party logistics providers who want to offer, seamless, built-in shipping functionality to their customers. 
<SchemaDefinition schemaRef="#/components/schemas/ShippoAccount"/>

### Available Operations

* [list](#list) - List all Shippo Accounts
* [create](#create) - Create a Shippo Account
* [get](#get) - Retrieve a Shippo Account
* [update](#update) - Update a Shippo Account

## list

Returns a list of Shippo Accounts objects

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.shippo_accounts.list()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                          | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `page`                                             | *Optional[int]*                                    | :heavy_minus_sign:                                 | The page number you want to select                 |
| `results`                                          | *Optional[int]*                                    | :heavy_minus_sign:                                 | The number of results to return per page (max 100) |

### Response

**[components.ShippoAccountPaginatedList](../../models/components/shippoaccountpaginatedlist.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |


## create

Creates a Shippo Account object

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.shippo_accounts.create(request=components.ShippoAccountUpdateRequest(
    email='hippo@shippo.com',
    first_name='Shippo',
    last_name='Meister',
    company_name='Acme',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [components.ShippoAccountUpdateRequest](../../models/components/shippoaccountupdaterequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |

### Response

**[components.ShippoAccount](../../models/components/shippoaccount.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |


## get

Returns a Shippo Account using an object ID

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.shippo_accounts.get(shippo_account_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                      | Type                           | Required                       | Description                    |
| ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ |
| `shippo_account_id`            | *str*                          | :heavy_check_mark:             | Object ID of the ShippoAccount |

### Response

**[components.ShippoAccount](../../models/components/shippoaccount.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |


## update

Updates a Shippo Account object

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.shippo_accounts.update(shippo_account_id='<value>', shippo_account_update_request=components.ShippoAccountUpdateRequest(
    email='hippo@shippo.com',
    first_name='Shippo',
    last_name='Meister',
    company_name='Acme',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `shippo_account_id`                                                                                      | *str*                                                                                                    | :heavy_check_mark:                                                                                       | Object ID of the ShippoAccount                                                                           |
| `shippo_account_update_request`                                                                          | [Optional[components.ShippoAccountUpdateRequest]](../../models/components/shippoaccountupdaterequest.md) | :heavy_minus_sign:                                                                                       | N/A                                                                                                      |

### Response

**[components.ShippoAccount](../../models/components/shippoaccount.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
