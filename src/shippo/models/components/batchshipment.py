"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from shippo.types import BaseModel
from typing import Any, List, Optional, TypedDict
from typing_extensions import NotRequired


class Status(str, Enum):
    r"""`INVALID` batch shipments cannot be purchased and will have to be removed, fixed, and added to the batch again.<br>
    `VALID` batch shipments can be purchased. <br>
    Batch shipments with the status `TRANSACTION_FAILED` were not able to be purchased and the error will be displayed on the message field<br>
    `INCOMPLETE` batch shipments have an issue with the Address and will need to be removed, fixed, and added to the batch again.
    """
    INVALID = "INVALID"
    VALID = "VALID"
    INCOMPLETE = "INCOMPLETE"
    TRANSACTION_FAILED = "TRANSACTION_FAILED"


class BatchShipmentTypedDict(TypedDict):
    object_id: str
    r"""Object ID of this batch shipment. Can be used in the remove_shipments endpoint."""
    shipment: str
    r"""Object ID of the shipment object created for this batch shipment."""
    status: Status
    r"""`INVALID` batch shipments cannot be purchased and will have to be removed, fixed, and added to the batch again.<br>
    `VALID` batch shipments can be purchased. <br>
    Batch shipments with the status `TRANSACTION_FAILED` were not able to be purchased and the error will be displayed on the message field<br>
    `INCOMPLETE` batch shipments have an issue with the Address and will need to be removed, fixed, and added to the batch again.
    """
    carrier_account: NotRequired[str]
    r"""Object ID of the carrier account to be used for this shipment (will override batch default)"""
    metadata: NotRequired[str]
    r"""A string of up to 100 characters that can be filled with any additional information you want
    to attach to the object.
    """
    servicelevel_token: NotRequired[str]
    r"""A token that sets the shipping method for the batch, overriding the batch default.
    Servicelevel tokens can be found <a href=\"#tag/Service-Levels\">in this list</a>
    or <a href=\"#operation/ListCarrierAccounts\">at this endpoint</a>.
    """
    messages: NotRequired[List[Any]]
    r"""List of Shipment and Transaction error messages."""
    transaction: NotRequired[str]
    r"""Object ID of the transaction object created for this batch shipment."""
    

class BatchShipment(BaseModel):
    object_id: str
    r"""Object ID of this batch shipment. Can be used in the remove_shipments endpoint."""
    shipment: str
    r"""Object ID of the shipment object created for this batch shipment."""
    status: Status
    r"""`INVALID` batch shipments cannot be purchased and will have to be removed, fixed, and added to the batch again.<br>
    `VALID` batch shipments can be purchased. <br>
    Batch shipments with the status `TRANSACTION_FAILED` were not able to be purchased and the error will be displayed on the message field<br>
    `INCOMPLETE` batch shipments have an issue with the Address and will need to be removed, fixed, and added to the batch again.
    """
    carrier_account: Optional[str] = None
    r"""Object ID of the carrier account to be used for this shipment (will override batch default)"""
    metadata: Optional[str] = None
    r"""A string of up to 100 characters that can be filled with any additional information you want
    to attach to the object.
    """
    servicelevel_token: Optional[str] = None
    r"""A token that sets the shipping method for the batch, overriding the batch default.
    Servicelevel tokens can be found <a href=\"#tag/Service-Levels\">in this list</a>
    or <a href=\"#operation/ListCarrierAccounts\">at this endpoint</a>.
    """
    messages: Optional[List[Any]] = None
    r"""List of Shipment and Transaction error messages."""
    transaction: Optional[str] = None
    r"""Object ID of the transaction object created for this batch shipment."""
    
