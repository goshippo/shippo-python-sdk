# <img src="https://docs.goshippo.com/images/Logo.png" width="30" alt="Shippo logo"> Shippo Python SDK 




Shippo is a shipping API that connects you with [multiple shipping carriers](https://goshippo.com/carriers) (such as USPS, UPS, DHL, Canada Post, Australia Post, and many others) through one interface.

You must register for a [Shippo account](https://apps.goshippo.com/join) to use our API. It's free to sign up. Only pay to print a live label, test labels are free.

To use the API, you must generate an [API Token](https://docs.goshippo.com/docs/guides_general/authentication/). In the following examples, replace `<YOUR_API_KEY_HERE>` with your own token.

For example.
```
api_key_header="ShippoToken shippo_test_595d9cb0c0e14497bf07e75ecfec6c6d"
```


<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install shippo
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


res = s.addresses.list_addresses(page=1, results=25)

if res.address_list_wrapper is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->

## Documentation
Review our full guides and references at [https://docs.goshippo.com/](https://docs.goshippo.com/).


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
<!-- No Error Handling [errors] -->

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

<!-- No Server Selection [server] -->
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
## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release.


## About Shippo
Connect with multiple different carriers, get discounted shipping labels, track parcels, and much more with just one integration. You can use your own carrier accounts or take advantage of our discounted rates with the Shippo carrier accounts. Using Shippo makes it easy to deal with multiple carrier integrations, rate shopping, tracking and other parts of the shipping workflow. We provide the API and web app for all your shipping needs.



<!-- Placeholder for Future Speakeasy SDK Sections -->
