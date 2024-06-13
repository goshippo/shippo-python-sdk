# <img src="https://docs.goshippo.com/images/Logo.png" width="30" alt="Shippo logo"> Shippo Python SDK 

Shippo is a shipping API that connects you with [multiple shipping carriers](https://goshippo.com/carriers) (such as USPS, UPS, DHL, Canada Post, Australia Post, and many others) through one interface.

You must register for a [Shippo account](https://apps.goshippo.com/join) to use our API. It's free to sign up. Only pay to print a live label, test labels are free.

To use the API, you must generate an [API Token](https://docs.goshippo.com/docs/guides_general/authentication/). In the following examples, replace `<YOUR_API_KEY_HERE>` with your own token.

For example.
```
api_key_header="shippo_test_595d9cb0c0e14497bf07e75ecfec6c6d"
```


<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install shippo
```
<!-- End SDK Installation [installation] -->

## SDK Reinstallation to a specific version

```bash
pip install --force-reinstall -I shippo==3.4.4
```

## SDK Example Usage

### Example

```python
import shippo

shippo_sdk = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    # the API version can be globally set, though this is normally not required
    # shippo_api_version='<YYYY-MM-DD>',
)

address_list = shippo_sdk.addresses.list()

if address_list is not None:
    # handle response
    pass
```
<!-- No SDK Example Usage [usage] -->
<!-- No Error Handling [errors] -->
<!-- No Server Selection [server] -->
<!-- No Authentication [security] -->
<!-- No Global Parameters [global-parameters] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import shippo
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = shippo.Shippo(client=http_client)
```
<!-- End Custom HTTP Client [http-client] -->

## Debug HTTP Client

The Shippo Python SDK returns schema models directly rather than wrapping the response in an envelope along with 
additional request/response details (status code, raw json, etc).  However, there are times when the underlying 
http information is useful so a 'debug' client is provided.  Using this client, you can retrieve the 
`requests.PreparedRequest` and `requests.Response` from the most recent API call.

```python
import shippo
from shippo.debug import DebugSession

debug_session = DebugSession()
shippo_sdk = shippo.Shippo(api_key_header="<YOUR_API_KEY_HERE>", client=debug_session)

shippo_sdk.addresses.list()

# print the previous request http headers
print(debug_session.last_request.headers)  
# print the previous response status code and raw json
print(debug_session.last_response.status_code, debug_session.last_response.text)
```

## Documentation
Review our full guides and references at [https://docs.goshippo.com/](https://docs.goshippo.com/).

<!-- Placeholder for Future Speakeasy SDK Sections -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [addresses](docs/sdks/addresses/README.md)

* [list](docs/sdks/addresses/README.md#list) - List all addresses
* [create](docs/sdks/addresses/README.md#create) - Create a new address
* [get](docs/sdks/addresses/README.md#get) - Retrieve an address
* [validate](docs/sdks/addresses/README.md#validate) - Validate an address

### [batches](docs/sdks/batches/README.md)

* [create](docs/sdks/batches/README.md#create) - Create a batch
* [get](docs/sdks/batches/README.md#get) - Retrieve a batch
* [add_shipments](docs/sdks/batches/README.md#add_shipments) - Add shipments to a batch
* [purchase](docs/sdks/batches/README.md#purchase) - Purchase a batch
* [remove_shipments](docs/sdks/batches/README.md#remove_shipments) - Remove shipments from a batch

### [carrier_accounts](docs/sdks/carrieraccounts/README.md)

* [list](docs/sdks/carrieraccounts/README.md#list) - List all carrier accounts
* [create](docs/sdks/carrieraccounts/README.md#create) - Create a new carrier account
* [get](docs/sdks/carrieraccounts/README.md#get) - Retrieve a carrier account
* [update](docs/sdks/carrieraccounts/README.md#update) - Update a carrier account
* [initiate_oauth2_signin](docs/sdks/carrieraccounts/README.md#initiate_oauth2_signin) - Connect an existing carrier account using OAuth 2.0
* [register](docs/sdks/carrieraccounts/README.md#register) - Add a Shippo carrier account
* [get_registration_status](docs/sdks/carrieraccounts/README.md#get_registration_status) - Get Carrier Registration status

### [customs_declarations](docs/sdks/customsdeclarations/README.md)

* [list](docs/sdks/customsdeclarations/README.md#list) - List all customs declarations
* [create](docs/sdks/customsdeclarations/README.md#create) - Create a new customs declaration
* [get](docs/sdks/customsdeclarations/README.md#get) - Retrieve a customs declaration

### [customs_items](docs/sdks/customsitems/README.md)

* [list](docs/sdks/customsitems/README.md#list) - List all customs items
* [create](docs/sdks/customsitems/README.md#create) - Create a new customs item
* [get](docs/sdks/customsitems/README.md#get) - Retrieve a customs item

### [rates_at_checkout](docs/sdks/ratesatcheckout/README.md)

* [create](docs/sdks/ratesatcheckout/README.md#create) - Generate a live rates request
* [get_default_parcel_template](docs/sdks/ratesatcheckout/README.md#get_default_parcel_template) - Show current default parcel template
* [update_default_parcel_template](docs/sdks/ratesatcheckout/README.md#update_default_parcel_template) - Update default parcel template
* [delete_default_parcel_template](docs/sdks/ratesatcheckout/README.md#delete_default_parcel_template) - Clear current default parcel template

### [manifests](docs/sdks/manifests/README.md)

* [list](docs/sdks/manifests/README.md#list) - List all manifests
* [create](docs/sdks/manifests/README.md#create) - Create a new manifest
* [get](docs/sdks/manifests/README.md#get) - Retrieve a manifest

### [orders](docs/sdks/orders/README.md)

* [list](docs/sdks/orders/README.md#list) - List all orders
* [create](docs/sdks/orders/README.md#create) - Create a new order
* [get](docs/sdks/orders/README.md#get) - Retrieve an order

### [carrier_parcel_templates](docs/sdks/carrierparceltemplates/README.md)

* [list](docs/sdks/carrierparceltemplates/README.md#list) - List all carrier parcel templates
* [get](docs/sdks/carrierparceltemplates/README.md#get) - Retrieve a carrier parcel templates

### [parcels](docs/sdks/parcels/README.md)

* [list](docs/sdks/parcels/README.md#list) - List all parcels
* [create](docs/sdks/parcels/README.md#create) - Create a new parcel
* [get](docs/sdks/parcels/README.md#get) - Retrieve an existing parcel

### [pickups](docs/sdks/pickups/README.md)

* [create](docs/sdks/pickups/README.md#create) - Create a pickup

### [rates](docs/sdks/rates/README.md)

* [get](docs/sdks/rates/README.md#get) - Retrieve a rate
* [list_shipment_rates](docs/sdks/rates/README.md#list_shipment_rates) - Retrieve shipment rates
* [list_shipment_rates_by_currency_code](docs/sdks/rates/README.md#list_shipment_rates_by_currency_code) - Retrieve shipment rates in currency

### [refunds](docs/sdks/refunds/README.md)

* [create](docs/sdks/refunds/README.md#create) - Create a refund
* [list](docs/sdks/refunds/README.md#list) - List all refunds
* [get](docs/sdks/refunds/README.md#get) - Retrieve a refund

### [service_groups](docs/sdks/servicegroups/README.md)

* [list](docs/sdks/servicegroups/README.md#list) - List all service groups
* [create](docs/sdks/servicegroups/README.md#create) - Create a new service group
* [update](docs/sdks/servicegroups/README.md#update) - Update an existing service group
* [delete](docs/sdks/servicegroups/README.md#delete) - Delete a service group

### [shipments](docs/sdks/shipments/README.md)

* [list](docs/sdks/shipments/README.md#list) - List all shipments
* [create](docs/sdks/shipments/README.md#create) - Create a new shipment
* [get](docs/sdks/shipments/README.md#get) - Retrieve a shipment

### [tracking_status](docs/sdks/trackingstatus/README.md)

* [create](docs/sdks/trackingstatus/README.md#create) - Register a tracking webhook
* [get](docs/sdks/trackingstatus/README.md#get) - Get a tracking status

### [transactions](docs/sdks/transactions/README.md)

* [list](docs/sdks/transactions/README.md#list) - List all shipping labels
* [create](docs/sdks/transactions/README.md#create) - Create a shipping label
* [get](docs/sdks/transactions/README.md#get) - Retrieve a shipping label

### [user_parcel_templates](docs/sdks/userparceltemplates/README.md)

* [list](docs/sdks/userparceltemplates/README.md#list) - List all user parcel templates
* [create](docs/sdks/userparceltemplates/README.md#create) - Create a new user parcel template
* [delete](docs/sdks/userparceltemplates/README.md#delete) - Delete a user parcel template
* [get](docs/sdks/userparceltemplates/README.md#get) - Retrieves a user parcel template
* [update](docs/sdks/userparceltemplates/README.md#update) - Update an existing user parcel template

### [shippo_accounts](docs/sdks/shippoaccounts/README.md)

* [list](docs/sdks/shippoaccounts/README.md#list) - List all Shippo Accounts
* [create](docs/sdks/shippoaccounts/README.md#create) - Create a Shippo Account
* [get](docs/sdks/shippoaccounts/README.md#get) - Retrieve a Shippo Account
* [update](docs/sdks/shippoaccounts/README.md#update) - Update a Shippo Account

### [webhooks](docs/sdks/webhooks/README.md)

* [create_webhook](docs/sdks/webhooks/README.md#create_webhook) - Create a new webhook
* [list_webhooks](docs/sdks/webhooks/README.md#list_webhooks) - List all webhooks
* [get_webhook](docs/sdks/webhooks/README.md#get_webhook) - Retrieve a specific webhook
* [update_webhook](docs/sdks/webhooks/README.md#update_webhook) - Update an existing webhook
* [delete_webhook](docs/sdks/webhooks/README.md#delete_webhook) - Delete a specific webhook
<!-- End Available Resources and Operations [operations] -->

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release.


## About Shippo
Connect with multiple different carriers, get discounted shipping labels, track parcels, and much more with just one integration. You can use your own carrier accounts or take advantage of our discounted rates with the Shippo carrier accounts. Using Shippo makes it easy to deal with multiple carrier integrations, rate shopping, tracking and other parts of the shipping workflow. We provide the API and web app for all your shipping needs.
