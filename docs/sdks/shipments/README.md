# Shipments
(*shipments*)

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

```python
import shippo
from shippo.models import operations

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.shipments.list(request=operations.ListShipmentsRequest())

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListShipmentsRequest](../../models/operations/listshipmentsrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |

### Response

**[components.ShipmentPaginatedList](../../models/components/shipmentpaginatedlist.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create

Creates a new shipment object.

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.shipments.create(request=components.ShipmentCreateRequest(
    address_from=components.AddressCreateRequest(
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
    ),
    address_to=components.AddressCreateRequest(
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
    ),
    parcels=[
        '<value>',
        components.ParcelCreateRequest(
            mass_unit=components.WeightUnitEnum.LB,
            weight='1',
            distance_unit=components.DistanceUnitEnum.IN,
            height='1',
            length='1',
            width='1',
            extra=components.ParcelExtra(
                cod=components.Cod(
                    amount='5.5',
                    currency='USD',
                    payment_method=components.PaymentMethod.CASH,
                ),
                insurance=components.ParcelInsurance(
                    amount='5.5',
                    content='Laptop',
                    currency='USD',
                    provider=components.ParcelInsuranceProvider.UPS,
                ),
            ),
            metadata='Customer ID 123456',
        ),
        components.ParcelCreateRequest(
            mass_unit=components.WeightUnitEnum.LB,
            weight='1',
            distance_unit=components.DistanceUnitEnum.IN,
            height='1',
            length='1',
            width='1',
            extra=components.ParcelExtra(
                cod=components.Cod(
                    amount='5.5',
                    currency='USD',
                    payment_method=components.PaymentMethod.CASH,
                ),
                insurance=components.ParcelInsurance(
                    amount='5.5',
                    content='Laptop',
                    currency='USD',
                    provider=components.ParcelInsuranceProvider.UPS,
                ),
            ),
            metadata='Customer ID 123456',
        ),
    ],
    extra=components.ShipmentExtra(
        accounts_receivable_customer_account=components.UPSReferenceFields(
            prefix='ABC',
            value='value',
            ref_sort=1,
        ),
        appropriation_number=components.UPSReferenceFields(
            prefix='ABC',
            value='value',
            ref_sort=1,
        ),
        bill_of_lading_number=components.UPSReferenceFields(
            prefix='ABC',
            value='value',
            ref_sort=1,
        ),
        cod=components.Cod(
            amount='5.5',
            currency='USD',
            payment_method=components.PaymentMethod.CASH,
        ),
        cod_number=components.UPSReferenceFields(
            prefix='ABC',
            value='value',
            ref_sort=1,
        ),
        customer_reference=components.CustomerReference(
            ref_sort=1,
        ),
        dealer_order_number=components.UPSReferenceFields(
            prefix='ABC',
            value='value',
            ref_sort=1,
        ),
        dept_number=components.DepartmentNumber(
            ref_sort=3,
        ),
        fda_product_code=components.UPSReferenceFields(
            prefix='ABC',
            value='value',
            ref_sort=1,
        ),
        insurance=components.Insurance(
            amount='5.5',
            currency='USD',
        ),
        invoice_number=components.InvoiceNumber(
            ref_sort=2,
        ),
        manifest_number=components.UPSReferenceFields(
            prefix='ABC',
            value='value',
            ref_sort=1,
        ),
        model_number=components.UPSReferenceFields(
            prefix='ABC',
            value='value',
            ref_sort=1,
        ),
        part_number=components.UPSReferenceFields(
            prefix='ABC',
            value='value',
            ref_sort=1,
        ),
        po_number=components.PoNumber(
            ref_sort=2,
        ),
        production_code=components.UPSReferenceFields(
            prefix='ABC',
            value='value',
            ref_sort=1,
        ),
        purchase_request_number=components.UPSReferenceFields(
            prefix='ABC',
            value='value',
            ref_sort=1,
        ),
        rma_number=components.RmaNumber(
            ref_sort=1,
        ),
        salesperson_number=components.UPSReferenceFields(
            prefix='ABC',
            value='value',
            ref_sort=1,
        ),
        serial_number=components.UPSReferenceFields(
            prefix='ABC',
            value='value',
            ref_sort=1,
        ),
        store_number=components.UPSReferenceFields(
            prefix='ABC',
            value='value',
            ref_sort=1,
        ),
        transaction_reference_number=components.UPSReferenceFields(
            prefix='ABC',
            value='value',
            ref_sort=1,
        ),
    ),
    metadata='Customer ID 123456',
    shipment_date='2021-03-22T12:00:00Z',
    address_return='d799c2679e644279b59fe661ac8fa488',
    customs_declaration=components.CustomsDeclarationCreateRequest(
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
    ),
    carrier_accounts=[
        '065a4a8c10d24a34ab932163a1b87f52',
        '73f706f4bdb94b54a337563840ce52b0',
    ],
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [components.ShipmentCreateRequest](../../models/components/shipmentcreaterequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |

### Response

**[components.Shipment](../../models/components/shipment.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get

Returns an existing shipment using an object ID

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.shipments.get(shipment_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                           | Type                                | Required                            | Description                         |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- |
| `shipment_id`                       | *str*                               | :heavy_check_mark:                  | Object ID of the shipment to update |

### Response

**[components.Shipment](../../models/components/shipment.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |