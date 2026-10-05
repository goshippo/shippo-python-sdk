# BatchStatus

- `VALIDATING`: the batch is being created and validated
- `VALID`: the batch can be purchased
- `INVALID`: the batch cannot be purchased; `INVALID` BatchShipments must be removed
- `PURCHASING`: the batch is being purchased
- `PURCHASED`: the batch is finished purchasing

## Example Usage

```python
from shippo.models.components import BatchStatus

value = BatchStatus.VALIDATING
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `VALIDATING` | VALIDATING   |
| `VALID`      | VALID        |
| `INVALID`    | INVALID      |
| `PURCHASING` | PURCHASING   |
| `PURCHASED`  | PURCHASED    |