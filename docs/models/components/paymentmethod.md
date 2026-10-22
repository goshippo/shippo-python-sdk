# PaymentMethod

Secured funds include money orders, certified cheques and others (see 
[UPS](https://www.ups.com/content/us/en/shipping/time/service/value_added/cod.html) for details). 
If no payment_method inputted the value defaults to "ANY".)

## Example Usage

```python
from shippo.models.components import PaymentMethod

value = PaymentMethod.SECURED_FUNDS
```


## Values

| Name            | Value           |
| --------------- | --------------- |
| `SECURED_FUNDS` | SECURED_FUNDS   |
| `CASH`          | CASH            |
| `ANY`           | ANY             |