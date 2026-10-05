# TransactionStatusEnum

Indicates the status of the Transaction.

## Example Usage

```python
from shippo.models.components import TransactionStatusEnum

value = TransactionStatusEnum.WAITING
```


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `WAITING`        | WAITING          |
| `QUEUED`         | QUEUED           |
| `SUCCESS`        | SUCCESS          |
| `ERROR`          | ERROR            |
| `REFUNDED`       | REFUNDED         |
| `REFUNDPENDING`  | REFUNDPENDING    |
| `REFUNDREJECTED` | REFUNDREJECTED   |