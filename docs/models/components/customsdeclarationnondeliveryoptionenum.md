# CustomsDeclarationNonDeliveryOptionEnum

Indicates how the carrier should proceed in case the shipment can't be delivered.
Allowed values available [here](/shippoapi/public-api/customs-declaration-non-delivery-option)

## Example Usage

```python
from shippo.models.components import CustomsDeclarationNonDeliveryOptionEnum

value = CustomsDeclarationNonDeliveryOptionEnum.ABANDON
```


## Values

| Name      | Value     |
| --------- | --------- |
| `ABANDON` | ABANDON   |
| `RETURN`  | RETURN    |