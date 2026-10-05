# CustomsDeclarationIncotermEnum

The incoterm reference of the shipment. FCA is available for DHL Express and FedEx only.
eDAP is available for DPD UK only. DAP is available for DHL Express, FedEx, and DPD UK.
If expecting DAP for other carriers, please use DDU.
Allowed values available [here](/shippoapi/public-api/customs-declaration-incoterm)
Carrier-specific restrictions are in the table below.

**Carrier-Specific Constraints:**
| Carrier | Constraints |
|:---|:---|
| FedEx | Must be one of DDP, DDU, FCA, DAP |

## Example Usage

```python
from shippo.models.components import CustomsDeclarationIncotermEnum

value = CustomsDeclarationIncotermEnum.DDP
```


## Values

| Name    | Value   |
| ------- | ------- |
| `DDP`   | DDP     |
| `DDU`   | DDU     |
| `FCA`   | FCA     |
| `DAP`   | DAP     |
| `E_DAP` | eDAP    |