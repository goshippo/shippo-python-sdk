# OrderStatusEnum

Current state of the order. See the [orders tutorial](https://docs.goshippo.com/docs/orders/orders/) 
for the logic of how the status is handled.

## Example Usage

```python
from shippo.models.components import OrderStatusEnum

value = OrderStatusEnum.UNKNOWN
```


## Values

| Name                  | Value                 |
| --------------------- | --------------------- |
| `UNKNOWN`             | UNKNOWN               |
| `AWAITPAY`            | AWAITPAY              |
| `PAID`                | PAID                  |
| `REFUNDED`            | REFUNDED              |
| `CANCELLED`           | CANCELLED             |
| `PARTIALLY_FULFILLED` | PARTIALLY_FULFILLED   |
| `SHIPPED`             | SHIPPED               |