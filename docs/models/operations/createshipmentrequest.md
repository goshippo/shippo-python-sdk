# CreateShipmentRequest


## Fields

| Field                                                                                          | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `shippo_api_version`                                                                           | *Optional[str]*                                                                                | :heavy_minus_sign:                                                                             | String used to pick a non-default API version to use                                           |
| `shipment_create_request`                                                                      | [Optional[components.ShipmentCreateRequest]](../../models/components/shipmentcreaterequest.md) | :heavy_minus_sign:                                                                             | Shipment details and contact info.                                                             |