<!-- Start SDK Example Usage [usage] -->
```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.addresses.list()

if res is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->