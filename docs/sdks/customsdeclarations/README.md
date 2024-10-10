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


res = s.customs_declarations.list()

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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

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
            hs_code='0901.21',
        ),
    ],
    non_delivery_option=components.CustomsDeclarationNonDeliveryOptionEnum.RETURN,
    b13a_filing_option=components.CustomsDeclarationB13AFilingOptionEnum.FILED_ELECTRONICALLY,
    contents_explanation='T-Shirt purchase',
    duties_payor=components.DutiesPayor(
        account='2323434543',
        type=components.CustomsDeclarationCreateRequestType.THIRD_PARTY,
        address=components.CustomsDeclarationCreateRequestAddress(
            name='Patrick Kavanagh',
            zip='80331',
            country='DE',
        ),
    ),
    exporter_identification=components.CustomsExporterIdentification(
        eori_number='PL123456790ABCDE',
        tax_id=components.CustomsTaxIdentification(
            number='123456789',
            type=components.CustomsTaxIdentificationType.EIN,
        ),
    ),
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
    eel_pfc=components.CustomsDeclarationEelPfcEnum.NOEEI_30_37_A,
    incoterm=components.CustomsDeclarationIncotermEnum.DDP,
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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get

Returns an existing customs declaration using an object ID

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.customs_declarations.get(customs_declaration_id='<value>')

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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |