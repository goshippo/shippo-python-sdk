"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .distanceunitenum import DistanceUnitEnum
from .parceltemplateenumset import ParcelTemplateEnumSet
from .weightunitenum import WeightUnitEnum
from dataclasses_json import Undefined, dataclass_json
from shippo import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ParcelCreateRequest:
    distance_unit: DistanceUnitEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('distance_unit') }})
    r"""The measure unit used for length, width and height."""
    height: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('height') }})
    r"""**Required if template is not specified**<br>
    Height of the parcel. Up to six digits in front and four digits after the decimal separator are accepted.
    """
    length: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('length') }})
    r"""**Required if template is not specified**<br>
    Length of the Parcel. Up to six digits in front and four digits after the decimal separator are accepted.
    """
    mass_unit: WeightUnitEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mass_unit') }})
    r"""The unit used for weight."""
    weight: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('weight') }})
    r"""Weight of the parcel. Up to six digits in front and four digits after the decimal separator are accepted."""
    width: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('width') }})
    r"""**Required if template is not specified**<br>
    Width of the Parcel. Up to six digits in front and four digits after the decimal separator are accepted.
    """
    template: Optional[ParcelTemplateEnumSet] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('template'), 'exclude': lambda f: f is None }})
    r"""If template is passed, `length`, `width`, `height`, and `distance_unit` are not required"""
    metadata: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    

