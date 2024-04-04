# Addresses
(*addresses*)

## Overview

Addresses are the locations a parcel is being shipped **from** and **to**. They represent company and residential places. Among other things, you can use address objects to create shipments, calculate shipping rates, and purchase shipping labels.
<SchemaDefinition schemaRef="#/components/schemas/Address"/>

### Available Operations

* [list](#list) - List all addresses
* [create](#create) - Create a new address
* [get](#get) - Retrieve an address
* [validate](#validate) - Validate an address

## list

Returns a list of all address objects that have been created in this account.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.addresses.list(page=1, results=25, shippo_api_version='2018-02-08')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `page`                                               | *Optional[int]*                                      | :heavy_minus_sign:                                   | The page number you want to select                   |                                                      |
| `results`                                            | *Optional[int]*                                      | :heavy_minus_sign:                                   | The number of results to return per page (max 100)   |                                                      |
| `shippo_api_version`                                 | *Optional[str]*                                      | :heavy_minus_sign:                                   | String used to pick a non-default API version to use | 2018-02-08                                           |


### Response

**[components.AddressPaginatedList](../../models/components/addresspaginatedlist.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create

Creates a new address object. You can use address objects to create new shipments, calculate rates, and to create orders.

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.addresses.create(shippo_api_version='2018-02-08', address_create_request=components.AddressCreateRequest(
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

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  | Example                                                                                      |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `shippo_api_version`                                                                         | *Optional[str]*                                                                              | :heavy_minus_sign:                                                                           | String used to pick a non-default API version to use                                         | 2018-02-08                                                                                   |
| `address_create_request`                                                                     | [Optional[components.AddressCreateRequest]](../../models/components/addresscreaterequest.md) | :heavy_minus_sign:                                                                           | Address details.                                                                             |                                                                                              |


### Response

**[components.Address](../../models/components/address.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get

Returns an existing address using an object ID.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.addresses.get(address_id='<value>', shippo_api_version='2018-02-08')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `address_id`                                         | *str*                                                | :heavy_check_mark:                                   | Object ID of the address                             |                                                      |
| `shippo_api_version`                                 | *Optional[str]*                                      | :heavy_minus_sign:                                   | String used to pick a non-default API version to use | 2018-02-08                                           |


### Response

**[components.Address](../../models/components/address.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## validate

Validates an existing address using an object ID

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.addresses.validate(address_id='<value>', shippo_api_version='2018-02-08')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `address_id`                                         | *str*                                                | :heavy_check_mark:                                   | Object ID of the address                             |                                                      |
| `shippo_api_version`                                 | *Optional[str]*                                      | :heavy_minus_sign:                                   | String used to pick a non-default API version to use | 2018-02-08                                           |


### Response

**[components.Address](../../models/components/address.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
