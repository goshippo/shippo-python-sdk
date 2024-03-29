<!-- Start SDK Example Usage [usage] -->
```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.addresses.list(page=1, results=25, shippo_api_version='<value>')

if res is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->