# TrackingStatusEnum

Indicates the high level status of the shipment.

## Example Usage

```python
from shippo.models.components import TrackingStatusEnum

value = TrackingStatusEnum.UNKNOWN
```


## Values

| Name          | Value         |
| ------------- | ------------- |
| `UNKNOWN`     | UNKNOWN       |
| `PRE_TRANSIT` | PRE_TRANSIT   |
| `TRANSIT`     | TRANSIT       |
| `DELIVERED`   | DELIVERED     |
| `RETURNED`    | RETURNED      |
| `FAILURE`     | FAILURE       |