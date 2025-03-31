<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from shippo import Shippo


with Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version="2018-02-08",
) as s_client:

    res = s_client.addresses.list()

    assert res is not None

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from shippo import Shippo

async def main():

    async with Shippo(
        api_key_header="<YOUR_API_KEY_HERE>",
        shippo_api_version="2018-02-08",
    ) as s_client:

        res = await s_client.addresses.list_async()

        assert res is not None

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->