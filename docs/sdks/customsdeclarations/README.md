# CustomsDeclarations
(*customs_declarations*)

## Overview

Customs declarations are relevant information, including one or multiple customs items, you need to provide for 
customs clearance for your international shipments.
<SchemaDefinition schemaRef="#/components/schemas/CustomsDeclaration"/>

### Available Operations

* [list](#list) - List all customs declarations
* [create](#create) - Create a new customs declaration
* [get](#get) - Retrieve a customs declaration

## list

Returns a a list of all customs declaration objects

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.customs_declarations.list(page=1, results=25, shippo_api_version='<value>')

if res is not None:
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

**[components.CustomsDeclarationPaginatedList](../../models/components/customsdeclarationpaginatedlist.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create

Creates a new customs declaration object

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.customs_declarations.create(shippo_api_version='<value>', customs_declaration_create_request=components.CustomsDeclarationCreateRequest(
    certify=True,
    certify_signer='Shawn Ippotle',
    contents_type=components.CustomsDeclarationCreateRequestContentsType.MERCHANDISE,
    non_delivery_option=components.CustomsDeclarationCreateRequestNonDeliveryOption.ABANDON,
    items=[
        components.CustomsItemBase(
            description='T-Shirt',
            mass_unit=components.WeightUnit.LB,
            net_weight='5',
            origin_country='<value>',
            quantity=20,
            value_amount='200',
            value_currency='USD',
            metadata='Order ID "123454"',
            sku_code='HM-123',
        ),
    ],
    contents_explanation='T-Shirt purchase',
    eel_pfc=components.CustomsDeclarationCreateRequestEelPfc.NOEEI_30_37_A,
    incoterm=components.CustomsDeclarationCreateRequestIncoterm.DDP,
    invoice='#123123',
    metadata='Order ID #123123',
    test=True,
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `shippo_api_version`                                                                                               | *Optional[str]*                                                                                                    | :heavy_minus_sign:                                                                                                 | String used to pick a non-default API version to use                                                               |
| `customs_declaration_create_request`                                                                               | [Optional[components.CustomsDeclarationCreateRequest]](../../models/components/customsdeclarationcreaterequest.md) | :heavy_minus_sign:                                                                                                 | CustomsDeclaration details.                                                                                        |


### Response

**[components.CustomsDeclaration](../../models/components/customsdeclaration.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get

Returns an existing customs declaration using an object ID

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.customs_declarations.get(customs_declaration_id='<value>', page=1, shippo_api_version='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `customs_declaration_id`                             | *str*                                                | :heavy_check_mark:                                   | Object ID of the customs declaration                 |
| `page`                                               | *Optional[int]*                                      | :heavy_minus_sign:                                   | The page number you want to select                   |
| `shippo_api_version`                                 | *Optional[str]*                                      | :heavy_minus_sign:                                   | String used to pick a non-default API version to use |


### Response

**[components.CustomsDeclaration](../../models/components/customsdeclaration.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
