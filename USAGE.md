<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from shippo import Shippo

s = Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version="2018-02-08",
)


res = s.addresses.list(page=1, results=5)

if res is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from shippo import Shippo

async def main():
    s = Shippo(
        api_key_header="<YOUR_API_KEY_HERE>",
        shippo_api_version="2018-02-08",
    )
    res = await s.addresses.list_async(page=1, results=5)
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->