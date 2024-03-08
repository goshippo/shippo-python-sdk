# shippo

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


## 🏗 **Welcome to your new SDK!** 🏗

It has been generated successfully based on your OpenAPI spec. However, it is not yet ready for production use. Here are some next steps:
- [ ] 🛠 Make your SDK feel handcrafted by [customizing it](https://www.speakeasyapi.dev/docs/customize-sdks)
- [ ] ♻️ Refine your SDK quickly by iterating locally with the [Speakeasy CLI](https://github.com/speakeasy-api/speakeasy)
- [ ] 🎁 Publish your SDK to package managers by [configuring automatic publishing](https://www.speakeasyapi.dev/docs/productionize-sdks/publish-sdks)
- [ ] ✨ When ready to productionize, delete this section from the README

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install git+<UNSET>.git
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.addresses.list_addresses(page=1, results=25, shippo_api_version='<value>')

if res.address_list_wrapper is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [addresses](docs/sdks/addresses/README.md)

* [list_addresses](docs/sdks/addresses/README.md#list_addresses) - List all addresses
* [create_address](docs/sdks/addresses/README.md#create_address) - Create a new address
* [get_address](docs/sdks/addresses/README.md#get_address) - Retrieve an address
* [validate_address](docs/sdks/addresses/README.md#validate_address) - Validate an address

### [batches](docs/sdks/batches/README.md)

* [create_batch](docs/sdks/batches/README.md#create_batch) - Create a batch
* [get_batch](docs/sdks/batches/README.md#get_batch) - Retrieve a batch
* [add_shipments_to_batch](docs/sdks/batches/README.md#add_shipments_to_batch) - Add shipments to a batch
* [purchase_batch](docs/sdks/batches/README.md#purchase_batch) - Purchase a batch
* [remove_shipments_from_batch](docs/sdks/batches/README.md#remove_shipments_from_batch) - Remove shipments from a batch

### [carrier_accounts](docs/sdks/carrieraccounts/README.md)

* [list_carrier_accounts](docs/sdks/carrieraccounts/README.md#list_carrier_accounts) - List all carrier accounts
* [create_carrier_account](docs/sdks/carrieraccounts/README.md#create_carrier_account) - Create a new carrier account
* [get_carrier_account](docs/sdks/carrieraccounts/README.md#get_carrier_account) - Retrieve a carrier account
* [update_carrier_account](docs/sdks/carrieraccounts/README.md#update_carrier_account) - Update a carrier account
* [register_carrier_account](docs/sdks/carrieraccounts/README.md#register_carrier_account) - Add a Shippo master carrier account
* [get_carrier_registration_status](docs/sdks/carrieraccounts/README.md#get_carrier_registration_status) - Get Carrier Registration status

### [customs_declarations](docs/sdks/customsdeclarations/README.md)

* [list_customs_declarations](docs/sdks/customsdeclarations/README.md#list_customs_declarations) - List all customs declarations
* [create_customs_declaration](docs/sdks/customsdeclarations/README.md#create_customs_declaration) - Create a new customs declaration
* [get_customs_declaration](docs/sdks/customsdeclarations/README.md#get_customs_declaration) - Retrieve a customs declaration

### [customs_items](docs/sdks/customsitems/README.md)

* [list_customs_items](docs/sdks/customsitems/README.md#list_customs_items) - List all customs items
* [create_customs_item](docs/sdks/customsitems/README.md#create_customs_item) - Create a new customs item
* [get_customs_item](docs/sdks/customsitems/README.md#get_customs_item) - Retrieve a customs item

### [invoices](docs/sdks/invoices/README.md)

* [get_invoice](docs/sdks/invoices/README.md#get_invoice) - Retrieve an invoice
* [list_invoices](docs/sdks/invoices/README.md#list_invoices) - List all invoices
* [list_invoice_items_template](docs/sdks/invoices/README.md#list_invoice_items_template) - List all invoice items

### [rates_at_checkout](docs/sdks/ratesatcheckout/README.md)

* [create_live_rate](docs/sdks/ratesatcheckout/README.md#create_live_rate) - Generate a live rates request
* [get_default_parcel_template](docs/sdks/ratesatcheckout/README.md#get_default_parcel_template) - Show current default parcel template
* [update_default_parcel_template](docs/sdks/ratesatcheckout/README.md#update_default_parcel_template) - Update default parcel template
* [delete_default_parcel_template](docs/sdks/ratesatcheckout/README.md#delete_default_parcel_template) - Clear current default parcel template

### [manifests](docs/sdks/manifests/README.md)

* [list_manifests](docs/sdks/manifests/README.md#list_manifests) - List all manifests
* [create_manifest](docs/sdks/manifests/README.md#create_manifest) - Create a new manifest
* [get_manifest](docs/sdks/manifests/README.md#get_manifest) - Retrieve a manifest

### [orders](docs/sdks/orders/README.md)

* [list_orders](docs/sdks/orders/README.md#list_orders) - List all orders
* [create_order](docs/sdks/orders/README.md#create_order) - Create a new order
* [get_order](docs/sdks/orders/README.md#get_order) - Retrieve an order

### [carrier_parcel_templates](docs/sdks/carrierparceltemplates/README.md)

* [list_carrier_parcel_templates](docs/sdks/carrierparceltemplates/README.md#list_carrier_parcel_templates) - List all carrier parcel templates
* [get_carrier_parcel_template](docs/sdks/carrierparceltemplates/README.md#get_carrier_parcel_template) - Retrieve a carrier parcel templates

### [parcels](docs/sdks/parcels/README.md)

* [list_parcels](docs/sdks/parcels/README.md#list_parcels) - List all parcels
* [create_parcel](docs/sdks/parcels/README.md#create_parcel) - Create a new parcel
* [get_parcel](docs/sdks/parcels/README.md#get_parcel) - Retrieve an existing parcel

### [pickups](docs/sdks/pickups/README.md)

* [create_pickup](docs/sdks/pickups/README.md#create_pickup) - Create a pickup

### [rates](docs/sdks/rates/README.md)

* [get_rate](docs/sdks/rates/README.md#get_rate) - Retrieve a rate
* [list_shipment_rates](docs/sdks/rates/README.md#list_shipment_rates) - Retrieve shipment rates
* [list_shipment_rates_by_currency_code](docs/sdks/rates/README.md#list_shipment_rates_by_currency_code) - Retrieve shipment rates in currency

### [refunds](docs/sdks/refunds/README.md)

* [create_refund](docs/sdks/refunds/README.md#create_refund) - Create a refund
* [list_refund](docs/sdks/refunds/README.md#list_refund) - List all refunds
* [get_refund](docs/sdks/refunds/README.md#get_refund) - Retrieve a refund

### [service_groups](docs/sdks/servicegroups/README.md)

* [list_service_groups](docs/sdks/servicegroups/README.md#list_service_groups) - List all service groups
* [create_service_group](docs/sdks/servicegroups/README.md#create_service_group) - Create a new service group
* [update_service_group](docs/sdks/servicegroups/README.md#update_service_group) - Update an existing service group
* [delete_service_group](docs/sdks/servicegroups/README.md#delete_service_group) - Delete a service group

### [shipments](docs/sdks/shipments/README.md)

* [list_shipments](docs/sdks/shipments/README.md#list_shipments) - List all shipments
* [create_shipment](docs/sdks/shipments/README.md#create_shipment) - Create a new shipment
* [get_shipment](docs/sdks/shipments/README.md#get_shipment) - Retrieve a shipment

### [tracking_status](docs/sdks/trackingstatus/README.md)

* [create_track](docs/sdks/trackingstatus/README.md#create_track) - Register a tracking webhook
* [get_track](docs/sdks/trackingstatus/README.md#get_track) - Get a tracking status

### [transactions](docs/sdks/transactions/README.md)

* [list_transactions](docs/sdks/transactions/README.md#list_transactions) - List all shipping labels
* [create_transaction](docs/sdks/transactions/README.md#create_transaction) - Create a shipping label
* [get_transaction](docs/sdks/transactions/README.md#get_transaction) - Retrieve a shipping label

### [user_parcel_templates](docs/sdks/userparceltemplates/README.md)

* [list_user_parcel_templates](docs/sdks/userparceltemplates/README.md#list_user_parcel_templates) - List all user parcel templates
* [create_user_parcel_template](docs/sdks/userparceltemplates/README.md#create_user_parcel_template) - Create a new user parcel template
* [delete_user_parcel_template](docs/sdks/userparceltemplates/README.md#delete_user_parcel_template) - Delete a user parcel template
* [get_user_parcel_template](docs/sdks/userparceltemplates/README.md#get_user_parcel_template) - Retrieves a user parcel template
* [update_user_parcel_template](docs/sdks/userparceltemplates/README.md#update_user_parcel_template) - Update an existing user parcel template

### [shippo_accounts](docs/sdks/shippoaccounts/README.md)

* [list_shippo_accounts](docs/sdks/shippoaccounts/README.md#list_shippo_accounts) - List all Shippo Accounts
* [create_shippo_account](docs/sdks/shippoaccounts/README.md#create_shippo_account) - Create a Shippo Account
* [get_shippo_account](docs/sdks/shippoaccounts/README.md#get_shippo_account) - Retrieve a Shippo Account
* [update_shippo_account](docs/sdks/shippoaccounts/README.md#update_shippo_account) - Update a Shippo Account
<!-- End Available Resources and Operations [operations] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object                                        | Status Code                                         | Content Type                                        |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| errors.PlatformCarrierOwnAccountCreation400Response | 400                                                 | application/json                                    |
| errors.SDKError                                     | 4x-5xx                                              | */*                                                 |

### Example

```python
import shippo
from shippo.models import components, errors

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = None
try:
    res = s.carrier_accounts.create_carrier_account(shippo_api_version='<value>', connect_existing_own_ups_account_request=components.ConnectExistingOwnUPSAccountRequest(
    account_id='<value>',
    active=False,
    parameters=components.UPSConnectExistingOwnAccountParameters(
        account_number='94567e',
        billing_address_city='San Francisco',
        billing_address_country_iso2='US',
        billing_address_state='CA',
        billing_address_street1='731 Market St',
        billing_address_zip='94103',
        collec_country_iso2='US',
        collec_zip='94103',
        company='Shippo',
        email='hippo@shippo.com',
        full_name='Shippo Meister',
        has_invoice=False,
        phone='1112223333',
        title='Manager',
        ups_agreements=False,
        aia_country_iso2='US',
        billing_address_street2='STE 200',
        currency_code='USD',
        invoice_controlid='1234',
        invoice_date='20210529',
        invoice_number='1112234',
        invoice_value='11.23',
    ),
    carrier='ups',
    metadata='UPS Account',
    test=False,
))
except errors.PlatformCarrierOwnAccountCreation400Response as e:
    # handle exception
    raise(e)
except errors.SDKError as e:
    # handle exception
    raise(e)

if res.carrier_account is not None:
    # handle response
    pass

```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://api.goshippo.com` | None |

#### Example

```python
import shippo

s = shippo.Shippo(
    server_idx=0,
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.addresses.list_addresses(page=1, results=25, shippo_api_version='<value>')

if res.address_list_wrapper is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import shippo

s = shippo.Shippo(
    server_url="https://api.goshippo.com",
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.addresses.list_addresses(page=1, results=25, shippo_api_version='<value>')

if res.address_list_wrapper is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import shippo
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = shippo.Shippo(client: http_client)
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name             | Type             | Scheme           |
| ---------------- | ---------------- | ---------------- |
| `api_key_header` | apiKey           | API key          |

To authenticate with the API the `api_key_header` parameter must be set when initializing the SDK client instance. For example:
```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.addresses.list_addresses(page=1, results=25, shippo_api_version='<value>')

if res.address_list_wrapper is not None:
    # handle response
    pass

```
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
