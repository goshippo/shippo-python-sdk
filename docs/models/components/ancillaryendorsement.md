# AncillaryEndorsement

Specify an ancillary service endorsement to provide the USPS with instructions on how to handle undeliverable-as-addressed pieces (DHL eCommerce only).

## Example Usage

```python
from shippo.models.components import AncillaryEndorsement

value = AncillaryEndorsement.FORWARDING_SERVICE_REQUESTED
```


## Values

| Name                           | Value                          |
| ------------------------------ | ------------------------------ |
| `FORWARDING_SERVICE_REQUESTED` | FORWARDING_SERVICE_REQUESTED   |
| `RETURN_SERVICE_REQUESTED`     | RETURN_SERVICE_REQUESTED       |