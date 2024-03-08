# Status

`INVALID` batch shipments cannot be purchased and will have to be removed, fixed, and added to the batch again.<br>
`VALID` batch shipments can be purchased. <br>
Batch shipments with the status `TRANSACTION_FAILED` were not able to be purchased and the error will be displayed on the message field<br> 
`INCOMPLETE` batch shipments have an issue with the Address and will need to be removed, fixed, and added to the batch again.


## Values

| Name                 | Value                |
| -------------------- | -------------------- |
| `INVALID`            | INVALID              |
| `VALID`              | VALID                |
| `INCOMPLETE`         | INCOMPLETE           |
| `TRANSACTION_FAILED` | TRANSACTION_FAILED   |