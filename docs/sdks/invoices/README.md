# Invoices
(*invoices*)

## Overview

<b> Please note that the following endpoints are in beta and API contract is subject to change. </b>
<br>
<br>
An invoice is a request for payment for Shippo services. It is a collection of invoice items. 
You can query your invoice at any time to see your current charges. 
Shippo sends invoices weekly or when your bill has exceeded $100.
<a href="https://support.goshippo.com/hc/en-us/articles/360024703991-Shippo-Billing-FAQs" target="blank">Shippo Billing FAQs</a>.
<SchemaDefinition schemaRef="#/components/schemas/Invoice"/>

# Invoice Item
Invoice items are the individual amounts owed to Shippo. They can represent a purchased label or a charge for a service. Invoice items also represent refunds. They are the line items in an invoice.
<SchemaDefinition schemaRef="#/components/schemas/InvoiceItem"/>

### Available Operations

* [get_invoice](#get_invoice) - Retrieve an invoice
* [list_invoices](#list_invoices) - List all invoices
* [list_invoice_items_template](#list_invoice_items_template) - List all invoice items

## get_invoice

<b> Endpoint is in beta and API contract is subject to change.</b> <br><br>Returns a single invoice using an object ID.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.invoices.get_invoice(invoice_object_id='<value>', shippo_api_version='<value>')

if res.invoice is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `invoice_object_id`                                  | *str*                                                | :heavy_check_mark:                                   | Object ID of the Invoice                             |
| `shippo_api_version`                                 | *Optional[str]*                                      | :heavy_minus_sign:                                   | String used to pick a non-default API version to use |


### Response

**[operations.GetInvoiceResponse](../../models/operations/getinvoiceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_invoices

<b> Endpoint is in beta and API contract is subject to change. </b> <br><br>
Retrieves a collection of invoices that belong to the authenticated user. 
Date range and invoice status filters can be used to filter the result set. The results are paginated. Please see
<a href="https://docs.goshippo.com/docs/api_concepts/filtering/" target="blank"> filtering documentation</a> for more information
on date filtering and pagination.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.invoices.list_invoices(page=1, results=25, shippo_api_version='<value>')

if res.invoice_list_wrapper is not None:
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

**[operations.ListInvoicesResponse](../../models/operations/listinvoicesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_invoice_items_template

<b> Endpoint is in beta and API contract is subject to change. </b> <br><br>
Retrieves a collection of invoice items that belong to the authenticated user. 
Invoice object ID and object owner object ID can be used to filter the result set.
The results are paginated. Please see <a href="https://docs.goshippo.com/docs/api_concepts/filtering/" target="blank"> filtering documentation</a> for more information
on date filtering and pagination.

### Example Usage

```python
import shippo
from shippo.models import operations

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)

req = operations.ListInvoiceItemsTemplateRequest()

res = s.invoices.list_invoice_items_template(req)

if res.invoice_item_list_wrapper is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.ListInvoiceItemsTemplateRequest](../../models/operations/listinvoiceitemstemplaterequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.ListInvoiceItemsTemplateResponse](../../models/operations/listinvoiceitemstemplateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
