# BuildingLocationType

Where your parcels will be available for pickup. "Security Deck" and "Shipping Dock" are only 
supported for DHL Express.

## Example Usage

```python
from shippo.models.components import BuildingLocationType

value = BuildingLocationType.BACK_DOOR
```


## Values

| Name            | Value           |
| --------------- | --------------- |
| `BACK_DOOR`     | Back Door       |
| `RING_BELL`     | Ring Bell       |
| `SECURITY_DECK` | Security Deck   |
| `SHIPPING_DOCK` | Shipping Dock   |
| `FRONT_DOOR`    | Front Door      |
| `KNOCK_ON_DOOR` | Knock on Door   |
| `IN_AT_MAILBOX` | In/At Mailbox   |
| `MAIL_ROOM`     | Mail Room       |
| `OFFICE`        | Office          |
| `OTHER`         | Other           |
| `RECEPTION`     | Reception       |
| `SIDE_DOOR`     | Side Door       |