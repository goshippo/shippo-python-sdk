"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .objectstateenum import ObjectStateEnum
from .weightunitenum import WeightUnitEnum
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from shippo import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CustomsItem:
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    r"""Text description of your item."""
    mass_unit: WeightUnitEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mass_unit') }})
    r"""The unit used for weight."""
    net_weight: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('net_weight') }})
    r"""Total weight of this item, i.e. quantity * weight per item."""
    origin_country: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('origin_country') }})
    r"""Country of origin of the item. Example: `US` or `DE`.
    All accepted values can be found on the <a href=\"http://www.iso.org/\" target=\"_blank\">Official ISO Website</a>.
    """
    quantity: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quantity') }})
    r"""Quantity of this item in the shipment you send.  Must be greater than 0."""
    value_amount: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value_amount') }})
    r"""Total value of this item, i.e. quantity * value per item."""
    value_currency: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value_currency') }})
    r"""Currency used for value_amount. The <a href=\\"http://www.xe.com/iso4217.php\\">official ISO 4217</a>
    currency codes are used, e.g.  `USD` or `EUR`.
    """
    eccn_ear99: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('eccn_ear99'), 'exclude': lambda f: f is None }})
    r"""Export Control Classification Number, required on some exports from the United States."""
    metadata: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    r"""A string of up to 100 characters that can be filled with any additional information you
    want to attach to the object.
    """
    sku_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sku_code'), 'exclude': lambda f: f is None }})
    r"""SKU code of the item, which is required by some carriers."""
    hs_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hs_code'), 'exclude': lambda f: f is None }})
    r"""HS code of the item, which is required by some carriers."""
    tariff_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tariff_number'), 'exclude': lambda f: f is None }})
    r"""The tariff number of the item."""
    object_created: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object_created'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""Date and time of object creation."""
    object_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object_id'), 'exclude': lambda f: f is None }})
    r"""Unique identifier of the given object."""
    object_owner: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object_owner'), 'exclude': lambda f: f is None }})
    r"""Username of the user who created the object."""
    object_state: Optional[ObjectStateEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object_state'), 'exclude': lambda f: f is None }})
    r"""Indicates the validity of the enclosing object"""
    object_updated: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object_updated'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""Date and time of last object update."""
    test: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('test'), 'exclude': lambda f: f is None }})
    r"""Indicates whether the object has been created in test mode."""
    

