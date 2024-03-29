<!-- Start SDK Example Usage [usage] -->
```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.addresses.list_addresses(page=1, results=25, shippo_api_version='<value>')

if res.address_paginated_list is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->