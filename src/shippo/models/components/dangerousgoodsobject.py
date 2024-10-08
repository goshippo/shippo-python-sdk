"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .dangerousgoodsbiologicalmaterial import DangerousGoodsBiologicalMaterial
from .dangerousgoodslithiumbatteries import DangerousGoodsLithiumBatteries
from dataclasses_json import Undefined, dataclass_json
from shippo import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DangerousGoodsObject:
    r"""Container for specifying the presence of dangerous materials. This is specific to USPS, and if any contents
    are provided, only certain USPS service levels will be eligible. For more information, see our
    <a href=\"https://docs.goshippo.com/docs/shipments/hazmat/\">guide on hazardous or dangerous materials shipping</a>.
    """
    contains: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('contains'), 'exclude': lambda f: f is None }})
    r"""Indicates if the shipment contains dangerous goods."""
    biological_material: Optional[DangerousGoodsBiologicalMaterial] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('biological_material'), 'exclude': lambda f: f is None }})
    r"""Container for specifying the presence of biological material."""
    lithium_batteries: Optional[DangerousGoodsLithiumBatteries] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lithium_batteries'), 'exclude': lambda f: f is None }})
    r"""Container for specifying the presence of lithium batteries."""
    

