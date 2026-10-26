# HealthcareHandling

Requests the carrier's healthcare handling program, where the carrier offers one. The rate returned keeps the carrier's
regular service level token.

**Carrier-Specific Constraints:**
| Carrier | Constraints |
|:---|:---|
| Purolator | Maps to Health Care+. Domestic Express services only (Express, Express 9AM, Express 10:30AM, Express Evening). Available to Purolator-approved accounts only. |


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `enabled`                                                                             | *Optional[bool]*                                                                      | :heavy_minus_sign:                                                                    | Set to `true` to request the carrier's healthcare handling program for this shipment. |