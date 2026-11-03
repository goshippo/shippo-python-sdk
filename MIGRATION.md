# Migrating from 3.x to 5.0

Version 5.0 of the `shippo` package is a major release with breaking changes. The SDK is now built on
Speakeasy's v2 Python generator, which uses [pydantic](https://docs.pydantic.dev/) models and the
[httpx](https://www.python-httpx.org/) HTTP client. This guide covers what you need to change when
upgrading from 3.x (the last release was 3.9.0).

Version 4.0.0 was never published. Upgrades go directly from 3.x to 5.0.

## Before you upgrade

- **Python 3.10 or newer is required.** On Python 3.9 or older, pip keeps installing 3.9.0.
- **Pin the old version if you are not ready.** For example, add `shippo~=3.9` or `shippo<5` to your requirements.
- **Try the beta first.** Pre-releases are only installed when you ask for one explicitly:

  ```bash
  pip install "shippo==5.0.0b1"
  ```

  Pin the exact version rather than using `pip install --pre shippo`. `--pre` also allows
  pre-release versions of every dependency, not just `shippo`.

## 1. Method arguments are keyword-only

All arguments must now be passed by name. Positional calls raise a `TypeError`.

```python
# 3.x
address = shippo_sdk.addresses.get("adr_123")
shipment = shippo_sdk.shipments.create(shipment_request)
addresses = shippo_sdk.addresses.list(1, 25)

# 5.0
address = shippo_sdk.addresses.get(address_id="adr_123")
shipment = shippo_sdk.shipments.create(request=shipment_request)
addresses = shippo_sdk.addresses.list(page=1, results=25)
```

## 2. Request bodies can be models or plain dicts

Every `request=` argument accepts either the model class or a plain `dict` with the same fields.

```python
from shippo.models import components

shippo_sdk.addresses.create(request=components.AddressCreateRequest(country="US", zip="94117"))
shippo_sdk.addresses.create(request={"country": "US", "zip": "94117"})
```

## 3. Methods whose arguments moved into a request body

These methods used to take individual arguments. They now take a single `request=`.

| 3.x | 5.0 |
| --- | --- |
| `refunds.create(transaction, async_=False)` | `refunds.create(request={"transaction": ..., "async_": False})` |
| `tracking_status.create(carrier, tracking_number, metadata=None)` | `tracking_status.create(request={"carrier": ..., "tracking_number": ...})` |
| `rates_at_checkout.update_default_parcel_template(object_id=...)` | `rates_at_checkout.update_default_parcel_template(request={"object_id": ...})` |

**Methods with no required parameters.** In 5.0.0b1 and 5.0.0b2, these methods required an empty
`request={}` argument. From 5.0.0b3 the argument is optional, so you can call them with no arguments
(passing `request={}` still works):

```python
shippo_sdk.service_groups.list()
shippo_sdk.refunds.list()
shippo_sdk.user_parcel_templates.list()
shippo_sdk.rates_at_checkout.get_default_parcel_template()
shippo_sdk.rates_at_checkout.delete_default_parcel_template()
```

## 4. Models are pydantic, not dataclasses

| 3.x (dataclasses-json) | 5.0 (pydantic) |
| --- | --- |
| `Address.from_dict(data)` | `Address.model_validate(data)` |
| `address.to_dict()` | `address.model_dump(by_alias=True, exclude_none=True)` |
| `address.to_json()` | `address.model_dump_json(by_alias=True, exclude_none=True)` |
| `dataclasses.replace(address, ...)` | `address.model_copy(update={...})` |

Each model also has a `TypedDict` counterpart (for example `AddressCreateRequestTypedDict`) that you
can use for type-checked dict requests.

## 5. The HTTP client is httpx, not requests

If you pass a custom client, use `httpx.Client` instead of `requests.Session`:

```python
# 3.x
import requests
session = requests.Session()
session.headers.update({"x-custom-header": "value"})
shippo_sdk = shippo.Shippo(api_key_header="<KEY>", client=session)

# 5.0
import httpx
shippo_sdk = shippo.Shippo(
    api_key_header="<KEY>",
    client=httpx.Client(headers={"x-custom-header": "value"}),
)
```

`shippo.debug.DebugSession` still works the same way. `last_request` and `last_response` are now
`httpx.Request` and `httpx.Response` objects.

## 6. Errors

`SDKError` is still raised for API errors, and it now inherits from `shippo.models.errors.ShippoError`.
`status_code`, `body`, and `raw_response` are still available. `raw_response` is now an
`httpx.Response`. If you construct `SDKError` yourself, for example in tests, its signature changed to
`SDKError(message, raw_response, body=None)`.

```python
from shippo.models.errors import ShippoError

try:
    shippo_sdk.addresses.get(address_id="adr_missing")
except ShippoError as e:
    print(e.status_code, e.body)
```

## New in 5.0

- **Async methods.** Every operation has an `*_async` variant, for example `await shippo_sdk.addresses.list_async()`.
- **Per-call options.** Every method accepts `retries=`, `timeout_ms=`, `server_url=`, and `http_headers=`.
- **Client-wide timeout.** `Shippo(timeout_ms=...)`.
- **Context manager.** Use `with Shippo(...) as shippo_sdk:` to close the HTTP client when you are done.
