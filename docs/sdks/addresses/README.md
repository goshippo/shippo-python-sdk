# Addresses
(*addresses*)

## Overview

Addresses are the locations a parcel is being shipped **from** and **to**. They represent company and residential places. Among other things, you can use address objects to create shipments, calculate shipping rates, and purchase shipping labels.
<SchemaDefinition schemaRef="#/components/schemas/Address"/>

### Available Operations

* [list_addresses](#list_addresses) - List all addresses
* [create_address](#create_address) - Create a new address
* [get_address](#get_address) - Retrieve an address
* [validate_address](#validate_address) - Validate an address

## list_addresses

Returns a list of all address objects that have been created in this account.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.addresses.list_addresses(page=1, results=25, shippo_api_version='<value>')

if res.address_paginated_list is not None:
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

**[operations.ListAddressesResponse](../../models/operations/listaddressesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_address

Creates a new address object. You can use address objects to create new shipments, calculate rates, and to create orders.

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.addresses.create_address(shippo_api_version='<value>', address_create_request=components.AddressCreateRequest(
    country='US',
    name='Shwan Ippotle',
    company='Shippo',
    street1='215 Clayton St.',
    street3='',
    street_no='',
    city='San Francisco',
    state='CA',
    zip='94117',
    phone='+1 555 341 9393',
    email='shippotle@shippo.com',
    is_residential=True,
    metadata='Customer ID 123456',
    validate=True,
))

if res.address is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `shippo_api_version`                                                                         | *Optional[str]*                                                                              | :heavy_minus_sign:                                                                           | String used to pick a non-default API version to use                                         |
| `address_create_request`                                                                     | [Optional[components.AddressCreateRequest]](../../models/components/addresscreaterequest.md) | :heavy_minus_sign:                                                                           | Address details.                                                                             |


### Response

**[operations.CreateAddressResponse](../../models/operations/createaddressresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_address

Returns an existing address using an object ID.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.addresses.get_address(address_id='<value>', shippo_api_version='<value>')

if res.address is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `address_id`                                         | *str*                                                | :heavy_check_mark:                                   | Object ID of the address                             |
| `shippo_api_version`                                 | *Optional[str]*                                      | :heavy_minus_sign:                                   | String used to pick a non-default API version to use |


### Response

**[operations.GetAddressResponse](../../models/operations/getaddressresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## validate_address

Validates an existing address using an object ID

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.addresses.validate_address(address_id='<value>', shippo_api_version='<value>')

if res.address is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `address_id`                                         | *str*                                                | :heavy_check_mark:                                   | Object ID of the address                             |
| `shippo_api_version`                                 | *Optional[str]*                                      | :heavy_minus_sign:                                   | String used to pick a non-default API version to use |


### Response

**[operations.ValidateAddressResponse](../../models/operations/validateaddressresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
