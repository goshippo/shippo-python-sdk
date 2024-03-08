"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .errormessage import ErrorMessage
from .shipmentcreaterequest import ShipmentCreateRequest
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from shippo import utils
from typing import List, Optional

class Status(str, Enum):
    r"""`INVALID` batch shipments cannot be purchased and will have to be removed, fixed, and added to the batch again.<br>
    `VALID` batch shipments can be purchased. <br>
    Batch shipments with the status `TRANSACTION_FAILED` were not able to be purchased and the error will be displayed on the message field<br> 
    `INCOMPLETE` batch shipments have an issue with the Address and will need to be removed, fixed, and added to the batch again.
    """
    INVALID = 'INVALID'
    VALID = 'VALID'
    INCOMPLETE = 'INCOMPLETE'
    TRANSACTION_FAILED = 'TRANSACTION_FAILED'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BatchShipment:
    shipment: ShipmentCreateRequest = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shipment') }})
    object_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object_id') }})
    r"""Object ID of this batch shipment. Can be used in the remove_shipments endpoint."""
    status: Status = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""`INVALID` batch shipments cannot be purchased and will have to be removed, fixed, and added to the batch again.<br>
    `VALID` batch shipments can be purchased. <br>
    Batch shipments with the status `TRANSACTION_FAILED` were not able to be purchased and the error will be displayed on the message field<br> 
    `INCOMPLETE` batch shipments have an issue with the Address and will need to be removed, fixed, and added to the batch again.
    """
    carrier_account: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('carrier_account'), 'exclude': lambda f: f is None }})
    r"""Object ID of the carrier account to be used for this shipment (will override batch default)"""
    metadata: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    r"""A string of up to 100 characters that can be filled with any additional information you want
    to attach to the object.
    """
    servicelevel_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('servicelevel_token'), 'exclude': lambda f: f is None }})
    r"""A token that sets the shipping method for the batch, overriding the batch default.
    Servicelevel tokens can be found <a href=\"#tag/Service-Levels\">in this list</a> 
    or <a href=\"#operation/ListCarrierAccounts\">at this endpoint</a>.
    """
    messages: Optional[List[ErrorMessage]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('messages'), 'exclude': lambda f: f is None }})
    r"""List of Shipment and Transaction error messages."""
    transaction: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transaction'), 'exclude': lambda f: f is None }})
    r"""Object ID of the transaction object created for this batch shipment."""
    

