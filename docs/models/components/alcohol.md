# Alcohol

Indicates that a shipment contains Alcohol (Fedex and UPS only).


## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `contains_alcohol`                                                              | *Optional[bool]*                                                                | :heavy_minus_sign:                                                              | Mandatory for Fedex and UPS. Specifies that the package contains Alcohol.       |
| `recipient_type`                                                                | [Optional[components.RecipientType]](../../models/components/recipienttype.md)  | :heavy_minus_sign:                                                              | Mandatory for Fedex only. License type of the recipient of the Alcohol Package. |