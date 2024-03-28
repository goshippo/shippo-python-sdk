# CustomsDeclarations
(*customs_declarations*)

## Overview

Customs declarations are relevant information, including one or multiple customs items, you need to provide for 
customs clearance for your international shipments.
<SchemaDefinition schemaRef="#/components/schemas/CustomsDeclaration"/>

### Available Operations

* [list_customs_declarations](#list_customs_declarations) - List all customs declarations
* [create_customs_declaration](#create_customs_declaration) - Create a new customs declaration
* [get_customs_declaration](#get_customs_declaration) - Retrieve a customs declaration

## list_customs_declarations

Returns a a list of all customs declaration objects

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.customs_declarations.list_customs_declarations(page=1, results=25, shippo_api_version='<value>')

if res.customs_declaration_paginated_list is not None:
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

**[operations.ListCustomsDeclarationsResponse](../../models/operations/listcustomsdeclarationsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_customs_declaration

Creates a new customs declaration object

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.customs_declarations.create_customs_declaration(shippo_api_version='<value>', customs_declaration_create_request=components.CustomsDeclarationCreateRequest(
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

if res.customs_declaration is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `shippo_api_version`                                                                                               | *Optional[str]*                                                                                                    | :heavy_minus_sign:                                                                                                 | String used to pick a non-default API version to use                                                               |
| `customs_declaration_create_request`                                                                               | [Optional[components.CustomsDeclarationCreateRequest]](../../models/components/customsdeclarationcreaterequest.md) | :heavy_minus_sign:                                                                                                 | CustomsDeclaration details.                                                                                        |


### Response

**[operations.CreateCustomsDeclarationResponse](../../models/operations/createcustomsdeclarationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_customs_declaration

Returns an existing customs declaration using an object ID

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.customs_declarations.get_customs_declaration(customs_declaration_id='<value>', page=1, shippo_api_version='<value>')

if res.customs_declaration is not None:
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

**[operations.GetCustomsDeclarationResponse](../../models/operations/getcustomsdeclarationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
