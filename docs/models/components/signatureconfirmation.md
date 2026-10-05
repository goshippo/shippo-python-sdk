# SignatureConfirmation

Request standard or adult signature confirmation. You can alternatively request Certified Mail (USPS only) 
or Indirect signature (FedEx only) or Carrier Confirmation (Deutsche Post only).

## Example Usage

```python
from shippo.models.components import SignatureConfirmation

value = SignatureConfirmation.STANDARD
```


## Values

| Name                   | Value                  |
| ---------------------- | ---------------------- |
| `STANDARD`             | STANDARD               |
| `ADULT`                | ADULT                  |
| `CERTIFIED`            | CERTIFIED              |
| `INDIRECT`             | INDIRECT               |
| `CARRIER_CONFIRMATION` | CARRIER_CONFIRMATION   |