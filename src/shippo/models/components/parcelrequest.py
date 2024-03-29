"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .distanceunittemplate import DistanceUnitTemplate
from .parcelextra import ParcelExtra
from .parceltemplateenumset import ParcelTemplateAramexAustralia, ParcelTemplateCouriersPlease, ParcelTemplateDHLeCommerce, ParcelTemplateDPDUK, ParcelTemplateFedEx, ParcelTemplateUPS, ParcelTemplateUSPS
from .weightunit import WeightUnit
from dataclasses_json import Undefined, dataclass_json
from shippo import utils
from typing import Optional, Union


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ParcelRequest:
    distance_unit: DistanceUnitTemplate = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('distance_unit') }})
    r"""The measure unit used for length, width and height. Required if template is not specified."""
    height: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('height') }})
    r"""Required if template is not specified. Height of the parcel. Up to six digits in front and four digits after the decimal separator are accepted."""
    length: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('length') }})
    r"""Required if template is not specified. Length of the Parcel. Up to six digits in front and four digits after the decimal separator are accepted."""
    mass_unit: WeightUnit = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mass_unit') }})
    r"""The unit used for weight."""
    weight: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('weight') }})
    r"""Weight of the parcel. Up to six digits in front and four digits after the decimal separator are accepted."""
    width: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('width') }})
    r"""Required if template is not specified. Width of the Parcel. Up to six digits in front and four digits after the decimal separator are accepted."""
    extra: Optional[ParcelExtra] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('extra'), 'exclude': lambda f: f is None }})
    r"""An object holding optional extra services to be requested for each parcel in a multi-piece shipment.
    See the <a href=\"#section/Parcel-Extras\">Parcel Extra table below</a> for all available services.
    """
    metadata: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    r"""A string of up to 100 characters that can be filled with any additional information you want to attach to the object."""
    template: Optional[Union[ParcelTemplateFedEx, ParcelTemplateUPS, ParcelTemplateUSPS, ParcelTemplateDHLeCommerce, ParcelTemplateDPDUK, ParcelTemplateCouriersPlease, ParcelTemplateAramexAustralia]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('template'), 'exclude': lambda f: f is None }})
    r"""If template is passed, `length`, `width`, `height`, and `distance_unit` are not required"""
    test: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('test'), 'exclude': lambda f: f is None }})
    r"""Indicates whether the object has been created in test mode."""
    

