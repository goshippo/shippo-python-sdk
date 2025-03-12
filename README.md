# <img src="https://docs.goshippo.com/images/Logo.png" width="30" alt="Shippo logo"> Shippo Python SDK 

Shippo is a shipping API that connects you with [multiple shipping carriers](https://goshippo.com/carriers) (such as USPS, UPS, DHL, Canada Post, Australia Post, and many others) through one interface.

You must register for a [Shippo account](https://apps.goshippo.com/join) to use our API. It's free to sign up. Only pay to print a live label, test labels are free.

To use the API, you must generate an [API Token](https://docs.goshippo.com/docs/guides_general/authentication/). In the following examples, replace `<YOUR_API_KEY_HERE>` with your own token.

For example.
```
api_key_header="shippo_test_595d9cb0c0e14497bf07e75ecfec6c6d"
```


<!-- Start Summary [summary] -->
## Summary

Shippo external API.: Use this API to integrate with the Shippo service
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [<img src="https://docs.goshippo.com/images/Logo.png" width="30" alt="Shippo logo"> Shippo Python SDK](#img-srchttpsdocsgoshippocomimageslogopng-width30-altshippo-logo-shippo-python-sdk)
  * [SDK Installation](#sdk-installation)
  * [SDK Reinstallation to a specific version](#sdk-reinstallation-to-a-specific-version)
  * [SDK Example Usage](#sdk-example-usage)
  * [Retries](#retries)
  * [Custom HTTP Client](#custom-http-client)
  * [Debug HTTP Client](#debug-http-client)
  * [Documentation](#documentation)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
  * [IDE Support](#ide-support)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Maturity](#maturity)
  * [Contributions](#contributions)
  * [About Shippo](#about-shippo)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install shippo
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add shippo
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from shippo python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "shippo",
# ]
# ///

from shippo import Shippo

sdk = Shippo(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
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

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from shippo import Shippo
from shippo.utils import BackoffStrategy, RetryConfig


with Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version="2018-02-08",
) as s_client:

    res = s_client.addresses.list(,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    assert res is not None

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from shippo import Shippo
from shippo.utils import BackoffStrategy, RetryConfig


with Shippo(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version="2018-02-08",
) as s_client:

    res = s_client.addresses.list()

    assert res is not None

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from shippo import Shippo
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Shippo(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from shippo import Shippo
from shippo.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Shippo(async_client=CustomClient(httpx.AsyncClient()))
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

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Shippo` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from shippo import Shippo
def main():

    with Shippo(
        api_key_header="<YOUR_API_KEY_HERE>",
        shippo_api_version="2018-02-08",
    ) as s_client:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Shippo(
        api_key_header="<YOUR_API_KEY_HERE>",
        shippo_api_version="2018-02-08",
    ) as s_client:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from shippo import Shippo
import logging

logging.basicConfig(level=logging.DEBUG)
s = Shippo(debug_logger=logging.getLogger("shippo"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

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

### [carrier_parcel_templates](docs/sdks/carrierparceltemplates/README.md)

* [list](docs/sdks/carrierparceltemplates/README.md#list) - List all carrier parcel templates
* [get](docs/sdks/carrierparceltemplates/README.md#get) - Retrieve a carrier parcel templates

### [customs_declarations](docs/sdks/customsdeclarations/README.md)

* [list](docs/sdks/customsdeclarations/README.md#list) - List all customs declarations
* [create](docs/sdks/customsdeclarations/README.md#create) - Create a new customs declaration
* [get](docs/sdks/customsdeclarations/README.md#get) - Retrieve a customs declaration

### [customs_items](docs/sdks/customsitems/README.md)

* [list](docs/sdks/customsitems/README.md#list) - List all customs items
* [create](docs/sdks/customsitems/README.md#create) - Create a new customs item
* [get](docs/sdks/customsitems/README.md#get) - Retrieve a customs item

### [manifests](docs/sdks/manifests/README.md)

* [list](docs/sdks/manifests/README.md#list) - List all manifests
* [create](docs/sdks/manifests/README.md#create) - Create a new manifest
* [get](docs/sdks/manifests/README.md#get) - Retrieve a manifest

### [orders](docs/sdks/orders/README.md)

* [list](docs/sdks/orders/README.md#list) - List all orders
* [create](docs/sdks/orders/README.md#create) - Create a new order
* [get](docs/sdks/orders/README.md#get) - Retrieve an order

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

### [rates_at_checkout](docs/sdks/ratesatcheckout/README.md)

* [create](docs/sdks/ratesatcheckout/README.md#create) - Generate a live rates request
* [get_default_parcel_template](docs/sdks/ratesatcheckout/README.md#get_default_parcel_template) - Show current default parcel template
* [update_default_parcel_template](docs/sdks/ratesatcheckout/README.md#update_default_parcel_template) - Update default parcel template
* [delete_default_parcel_template](docs/sdks/ratesatcheckout/README.md#delete_default_parcel_template) - Clear current default parcel template

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


### [shippo_accounts](docs/sdks/shippoaccounts/README.md)

* [list](docs/sdks/shippoaccounts/README.md#list) - List all Shippo Accounts
* [create](docs/sdks/shippoaccounts/README.md#create) - Create a Shippo Account
* [get](docs/sdks/shippoaccounts/README.md#get) - Retrieve a Shippo Account
* [update](docs/sdks/shippoaccounts/README.md#update) - Update a Shippo Account

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

### [webhooks](docs/sdks/webhooks/README.md)

* [create_webhook](docs/sdks/webhooks/README.md#create_webhook) - Create a new webhook
* [list_webhooks](docs/sdks/webhooks/README.md#list_webhooks) - List all webhooks
* [get_webhook](docs/sdks/webhooks/README.md#get_webhook) - Retrieve a specific webhook
* [update_webhook](docs/sdks/webhooks/README.md#update_webhook) - Update an existing webhook
* [delete_webhook](docs/sdks/webhooks/README.md#delete_webhook) - Delete a specific webhook

</details>
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
