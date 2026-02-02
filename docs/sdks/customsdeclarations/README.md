# CustomsDeclarations

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

<!-- UsageSnippet language="python" operationID="ListCustomsDeclarations" method="get" path="/customs/declarations" -->
```python
from shippo import Shippo


with Shippo(
    shippo_api_version="2018-02-08",
    api_key_header="<YOUR_API_KEY_HERE>",
) as s_client:

    res = s_client.customs_declarations.list(page=1, results=5)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The page number you want to select                                  |
| `results`                                                           | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The number of results to return per page (max 100, default 5)       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[components.CustomsDeclarationPaginatedList](../../models/components/customsdeclarationpaginatedlist.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create

Creates a new customs declaration object

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateCustomsDeclaration" method="post" path="/customs/declarations" -->
```python
from shippo import Shippo
from shippo.models import components


with Shippo(
    shippo_api_version="2018-02-08",
    api_key_header="<YOUR_API_KEY_HERE>",
) as s_client:

    res = s_client.customs_declarations.create(request={
        "b13a_filing_option": components.CustomsDeclarationB13AFilingOptionEnum.FILED_ELECTRONICALLY,
        "certify": True,
        "certify_signer": "Shawn Ippotle",
        "contents_explanation": "T-Shirt purchase",
        "duties_payor": {
            "account": "2323434543",
            "type": components.CustomsDeclarationCreateRequestType.THIRD_PARTY,
            "address": {
                "name": "Patrick Kavanagh",
                "zip": "80331",
                "country": "DE",
            },
        },
        "exporter_identification": {
            "eori_number": "PL123456790ABCDE",
            "tax_id": {
                "number": "123456789",
                "type": components.CustomsTaxIdentificationType.EIN,
            },
        },
        "invoice": "#123123",
        "metadata": "Order ID #123123",
        "address_importer": {
            "name": "Shwan Ippotle",
            "company": "Shippo",
            "street1": "Blumenstraße",
            "street3": "",
            "street_no": "22",
            "city": "München",
            "state": "CA",
            "zip": "80331",
            "country": "DE",
            "phone": "80331",
            "email": "shippotle@shippo.com",
            "is_residential": True,
        },
        "contents_type": components.CustomsDeclarationContentsTypeEnum.MERCHANDISE,
        "eel_pfc": components.CustomsDeclarationEelPfcEnum.NOEEI_30_37_A,
        "incoterm": components.CustomsDeclarationIncotermEnum.DDP,
        "items": [],
        "non_delivery_option": components.CustomsDeclarationNonDeliveryOptionEnum.RETURN,
        "test": True,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [components.CustomsDeclarationCreateRequest](../../models/components/customsdeclarationcreaterequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[components.CustomsDeclaration](../../models/components/customsdeclaration.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get

Returns an existing customs declaration using an object ID

### Example Usage

<!-- UsageSnippet language="python" operationID="GetCustomsDeclaration" method="get" path="/customs/declarations/{CustomsDeclarationId}" -->
```python
from shippo import Shippo


with Shippo(
    shippo_api_version="2018-02-08",
    api_key_header="<YOUR_API_KEY_HERE>",
) as s_client:

    res = s_client.customs_declarations.get(customs_declaration_id="<id>", page=1)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `customs_declaration_id`                                            | *str*                                                               | :heavy_check_mark:                                                  | Object ID of the customs declaration                                |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The page number you want to select                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[components.CustomsDeclaration](../../models/components/customsdeclaration.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |