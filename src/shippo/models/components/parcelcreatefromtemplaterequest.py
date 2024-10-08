"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .parcelextra import ParcelExtra
from .parceltemplateenumset import ParcelTemplateEnumSet
from .weightunitenum import WeightUnitEnum
from dataclasses_json import Undefined, dataclass_json
from shippo import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ParcelCreateFromTemplateRequest:
    mass_unit: WeightUnitEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mass_unit') }})
    r"""The unit used for weight."""
    weight: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('weight') }})
    r"""Weight of the parcel. Up to six digits in front and four digits after the decimal separator are accepted."""
    template: ParcelTemplateEnumSet = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('template') }})
    r"""If template is passed, `length`, `width`, `height`, and `distance_unit` are not required"""
    extra: Optional[ParcelExtra] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('extra'), 'exclude': lambda f: f is None }})
    r"""An object holding optional extra services to be requested for each parcel in a multi-piece shipment.
    See the <a href=\"#section/Parcel-Extras\">Parcel Extra table below</a> for all available services.
    """
    metadata: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    

