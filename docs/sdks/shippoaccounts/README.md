# ShippoAccounts
(*shippo_accounts*)

## Overview

Shippo Accounts are used by Shippo Platform Accounts to create and manage Managed Shippo Accounts. 
Managed Shippo Accounts are headless accounts that represent your customers. They are opaque to your end customers, meaning customers do not need to create their own Shippo login or have a billing relationship with Shippo. 
They can be used by marketplaces, e-commerce platforms, and third-party logistics providers who want to offer, seamless, built-in shipping functionality to their customers. 
<SchemaDefinition schemaRef="#/components/schemas/ShippoAccount"/>

### Available Operations

* [list_shippo_accounts](#list_shippo_accounts) - List all Shippo Accounts
* [create_shippo_account](#create_shippo_account) - Create a Shippo Account
* [get_shippo_account](#get_shippo_account) - Retrieve a Shippo Account
* [update_shippo_account](#update_shippo_account) - Update a Shippo Account

## list_shippo_accounts

Returns a list of Shippo Accounts objects

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.shippo_accounts.list_shippo_accounts(page=1, results=25, shippo_api_version='<value>')

if res.paginated_shippo_account_response is not None:
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

**[operations.ListShippoAccountsResponse](../../models/operations/listshippoaccountsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_shippo_account

Creates a Shippo Account object

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.shippo_accounts.create_shippo_account(shippo_api_version='<value>', base_shippo_account_struct=components.BaseShippoAccountStruct(
    email='hippo@shippo.com',
    first_name='Shippo',
    last_name='Meister',
    company_name='Acme',
))

if res.shippo_account is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `shippo_api_version`                                                                               | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | String used to pick a non-default API version to use                                               |
| `base_shippo_account_struct`                                                                       | [Optional[components.BaseShippoAccountStruct]](../../models/components/baseshippoaccountstruct.md) | :heavy_minus_sign:                                                                                 | Shippo Account details and contact info.                                                           |


### Response

**[operations.CreateShippoAccountResponse](../../models/operations/createshippoaccountresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_shippo_account

Returns a Shippo Account using an object ID

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.shippo_accounts.get_shippo_account(shippo_account_id='<value>', shippo_api_version='<value>')

if res.shippo_account is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `shippo_account_id`                                  | *str*                                                | :heavy_check_mark:                                   | Object ID of the ShippoAccount                       |
| `shippo_api_version`                                 | *Optional[str]*                                      | :heavy_minus_sign:                                   | String used to pick a non-default API version to use |


### Response

**[operations.GetShippoAccountResponse](../../models/operations/getshippoaccountresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_shippo_account

Updates a Shippo Account object

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.shippo_accounts.update_shippo_account(shippo_account_id='<value>', shippo_api_version='<value>', base_shippo_account_struct=components.BaseShippoAccountStruct(
    email='hippo@shippo.com',
    first_name='Shippo',
    last_name='Meister',
    company_name='Acme',
))

if res.shippo_account is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `shippo_account_id`                                                                                | *str*                                                                                              | :heavy_check_mark:                                                                                 | Object ID of the ShippoAccount                                                                     |
| `shippo_api_version`                                                                               | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | String used to pick a non-default API version to use                                               |
| `base_shippo_account_struct`                                                                       | [Optional[components.BaseShippoAccountStruct]](../../models/components/baseshippoaccountstruct.md) | :heavy_minus_sign:                                                                                 | Shippo Account details and contact info.                                                           |


### Response

**[operations.UpdateShippoAccountResponse](../../models/operations/updateshippoaccountresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
