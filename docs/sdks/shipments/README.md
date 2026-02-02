# Shipments

## Overview

A shipment is the act of transporting goods. A shipment object contains **to** and **from** addresses, and the parcel details that you are shipping. You can use the shipment object to retrieve shipping rates and purchase a shipping label.
<SchemaDefinition schemaRef="#/components/schemas/Shipment"/>
 
# Shipment Extras
The following values are supported for the `extra` field of the shipment object.
<SchemaDefinition schemaRef="#/components/schemas/ShipmentExtra"/>

### Available Operations

* [list](#list) - List all shipments
* [create](#create) - Create a new shipment
* [get](#get) - Retrieve a shipment

## list

Returns a list of all shipment objects.<br><br>
In order to filter results, you must use the below path parameters. 
A maximum date range of 90 days is permitted. 
Provided dates should be ISO 8601 UTC dates (timezone offsets are currently not supported).<br><br>

Optional path parameters:<br>
  `object_created_gt`- object(s) created greater than a provided date time<br>
  `object_created_gte` - object(s) created greater than or equal to a provided date time<br>
  `object_created_lt` - object(s) created less than a provided date time<br>
  `object_created_lte` - object(s) created less than or equal to a provided date time<br>

  Date format examples:<br>
    `2017-01-01`<br>
    `2017-01-01T03:30:30` or `2017-01-01T03:30:30.5`<br>
    `2017-01-01T03:30:30Z`<br><br>

  Example URL:<br>
    `https://api.goshippo.com/shipments/?object_created_gte=2017-01-01T00:00:30&object_created_lt=2017-04-01T00:00:30`

### Example Usage

<!-- UsageSnippet language="python" operationID="ListShipments" method="get" path="/shipments" -->
```python
from shippo import Shippo


with Shippo(
    shippo_api_version="2018-02-08",
    api_key_header="<YOUR_API_KEY_HERE>",
) as s_client:

    res = s_client.shipments.list(request={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListShipmentsRequest](../../models/operations/listshipmentsrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[components.ShipmentPaginatedList](../../models/components/shipmentpaginatedlist.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create

Creates a new shipment object.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateShipment" method="post" path="/shipments" -->
```python
from shippo import Shippo
from shippo.models import components


with Shippo(
    shippo_api_version="2018-02-08",
    api_key_header="<YOUR_API_KEY_HERE>",
) as s_client:

    res = s_client.shipments.create(request=components.ShipmentCreateRequest(
        extra=components.ShipmentExtra(
            accounts_receivable_customer_account=components.UPSReferenceFields(
                prefix="ABC",
                value="value",
                ref_sort=1,
            ),
            appropriation_number=components.UPSReferenceFields(
                prefix="ABC",
                value="value",
                ref_sort=1,
            ),
            bill_of_lading_number=components.UPSReferenceFields(
                prefix="ABC",
                value="value",
                ref_sort=1,
            ),
            cod=components.Cod(
                amount="5.5",
                currency="USD",
                payment_method=components.PaymentMethod.CASH,
            ),
            cod_number=components.UPSReferenceFields(
                prefix="ABC",
                value="value",
                ref_sort=1,
            ),
            customer_reference=components.CustomerReference(
                ref_sort=1,
            ),
            dealer_order_number=components.UPSReferenceFields(
                prefix="ABC",
                value="value",
                ref_sort=1,
            ),
            dept_number=components.DepartmentNumber(
                ref_sort=3,
            ),
            fda_product_code=components.UPSReferenceFields(
                prefix="ABC",
                value="value",
                ref_sort=1,
            ),
            insurance=components.Insurance(
                amount="5.5",
                currency="USD",
            ),
            invoice_number=components.InvoiceNumber(
                ref_sort=2,
            ),
            manifest_number=components.UPSReferenceFields(
                prefix="ABC",
                value="value",
                ref_sort=1,
            ),
            model_number=components.UPSReferenceFields(
                prefix="ABC",
                value="value",
                ref_sort=1,
            ),
            part_number=components.UPSReferenceFields(
                prefix="ABC",
                value="value",
                ref_sort=1,
            ),
            po_number=components.PoNumber(
                ref_sort=2,
            ),
            production_code=components.UPSReferenceFields(
                prefix="ABC",
                value="value",
                ref_sort=1,
            ),
            purchase_request_number=components.UPSReferenceFields(
                prefix="ABC",
                value="value",
                ref_sort=1,
            ),
            rma_number=components.RmaNumber(
                ref_sort=1,
            ),
            salesperson_number=components.UPSReferenceFields(
                prefix="ABC",
                value="value",
                ref_sort=1,
            ),
            serial_number=components.UPSReferenceFields(
                prefix="ABC",
                value="value",
                ref_sort=1,
            ),
            store_number=components.UPSReferenceFields(
                prefix="ABC",
                value="value",
                ref_sort=1,
            ),
            transaction_reference_number=components.UPSReferenceFields(
                prefix="ABC",
                value="value",
                ref_sort=1,
            ),
        ),
        metadata="Customer ID 123456",
        shipment_date="2021-03-22T12:00:00Z",
        address_from="d799c2679e644279b59fe661ac8fa488",
        address_return="d799c2679e644279b59fe661ac8fa488",
        address_to="d799c2679e644279b59fe661ac8fa489",
        customs_declaration="adcfdddf8ec64b84ad22772bce3ea37a",
        carrier_accounts=[
            "065a4a8c10d24a34ab932163a1b87f52",
            "73f706f4bdb94b54a337563840ce52b0",
        ],
        parcels=[
            "<value>",
        ],
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [components.ShipmentCreateRequest](../../models/components/shipmentcreaterequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[components.Shipment](../../models/components/shipment.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get

Returns an existing shipment using an object ID

### Example Usage

<!-- UsageSnippet language="python" operationID="GetShipment" method="get" path="/shipments/{ShipmentId}" -->
```python
from shippo import Shippo


with Shippo(
    shippo_api_version="2018-02-08",
    api_key_header="<YOUR_API_KEY_HERE>",
) as s_client:

    res = s_client.shipments.get(shipment_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `shipment_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Object ID of the shipment to update                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[components.Shipment](../../models/components/shipment.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |