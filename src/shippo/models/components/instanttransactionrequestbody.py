"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .labelfiletypeenum import LabelFileTypeEnum
from .shipmentcreaterequest import ShipmentCreateRequest
from dataclasses_json import Undefined, dataclass_json
from shippo import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InstantTransactionRequestBody:
    carrier_account: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('carrier_account') }})
    servicelevel_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('servicelevel_token') }})
    shipment: ShipmentCreateRequest = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shipment') }})
    label_file_type: Optional[LabelFileTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('label_file_type'), 'exclude': lambda f: f is None }})
    r"""Print format of the <a href=\\"https://docs.goshippo.com/docs/shipments/shippinglabelsizes/\\">label</a>. If empty, will use the default format set from
    <a href=\"https://apps.goshippo.com/settings/labels\">the Shippo dashboard.</a>
    """
    metadata: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    

