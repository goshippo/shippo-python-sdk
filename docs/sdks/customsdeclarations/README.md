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
    shippo_api_version='2018-02-08',
)

res = s.customs_declarations.list(page=1, results=5)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                     | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `page`                                                        | *Optional[int]*                                               | :heavy_minus_sign:                                            | The page number you want to select                            |
| `results`                                                     | *Optional[int]*                                               | :heavy_minus_sign:                                            | The number of results to return per page (max 100, default 5) |


### Response

**[components.CustomsDeclarationPaginatedList](../../models/components/customsdeclarationpaginatedlist.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create

Creates a new customs declaration object

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)

res = s.customs_declarations.create(request=components.CustomsDeclarationCreateRequest(
    certify=True,
    certify_signer='Shawn Ippotle',
    contents_type=components.CustomsDeclarationContentsTypeEnum.MERCHANDISE,
    non_delivery_option=components.CustomsDeclarationNonDeliveryOptionEnum.ABANDON,
    items=[
        components.CustomsItemCreateRequest(
            description='T-Shirt',
            mass_unit=components.WeightUnitEnum.LB,
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
    eel_pfc=components.CustomsDeclarationEelPfcEnum.NOEEI_30_37_A,
    incoterm=components.CustomsDeclarationIncotermEnum.DDP,
    invoice='#123123',
    metadata='Order ID #123123',
    address_importer=components.AddressImporter(
        name='Shwan Ippotle',
        company='Shippo',
        street1='Blumenstraße',
        street3='',
        street_no='22',
        city='München',
        state='CA',
        zip='80331',
        country='DE',
        phone='80331',
        email='shippotle@shippo.com',
        is_residential=True,
    ),
    test=True,
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [components.CustomsDeclarationCreateRequest](../../models/components/customsdeclarationcreaterequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[components.CustomsDeclaration](../../models/components/customsdeclaration.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get

Returns an existing customs declaration using an object ID

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)

res = s.customs_declarations.get(customs_declaration_id='<value>', page=1)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                            | Type                                 | Required                             | Description                          |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `customs_declaration_id`             | *str*                                | :heavy_check_mark:                   | Object ID of the customs declaration |
| `page`                               | *Optional[int]*                      | :heavy_minus_sign:                   | The page number you want to select   |


### Response

**[components.CustomsDeclaration](../../models/components/customsdeclaration.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
