# CustomsDeclarationB13AFilingOptionEnum

B13A Option details are obtained by filing a B13A Canada Export Declaration via the Canadian Export Reporting System (CERS). 
[More information on reporting commercial exports from Canada.](https://www.cbsa-asfc.gc.ca/services/export/guide-eng.html)
Allowed values available [here](/shippoapi/public-api/customs-declaration-b13a-filing-option)

## Example Usage

```python
from shippo.models.components import CustomsDeclarationB13AFilingOptionEnum

value = CustomsDeclarationB13AFilingOptionEnum.FILED_ELECTRONICALLY
```


## Values

| Name                   | Value                  |
| ---------------------- | ---------------------- |
| `FILED_ELECTRONICALLY` | FILED_ELECTRONICALLY   |
| `SUMMARY_REPORTING`    | SUMMARY_REPORTING      |
| `NOT_REQUIRED`         | NOT_REQUIRED           |