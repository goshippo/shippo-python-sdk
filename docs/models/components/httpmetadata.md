# HTTPMetadata


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `response`                                                                            | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) | :heavy_check_mark:                                                                    | Raw HTTP response; suitable for custom response parsing                               |
| `request`                                                                             | [requests.Request](https://requests.readthedocs.io/en/latest/api/#requests.Request)   | :heavy_check_mark:                                                                    | Raw HTTP request; suitable for debugging                                              |