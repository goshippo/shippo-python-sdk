# InsuranceProvider

To have insurance cover provided by a carrier directly instead of Shippo's provider (XCover), set `provider` to `FEDEX`, `UPS`, or `ONTRAC`.

## Example Usage

```python
from shippo.models.components import InsuranceProvider

value = InsuranceProvider.FEDEX
```


## Values

| Name     | Value    |
| -------- | -------- |
| `FEDEX`  | FEDEX    |
| `UPS`    | UPS      |
| `ONTRAC` | ONTRAC   |