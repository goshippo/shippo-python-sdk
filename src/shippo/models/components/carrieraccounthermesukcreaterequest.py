"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from shippo import utils


@dataclasses.dataclass
class CarrierAccountHermesUKCreateRequestParameters:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CarrierAccountHermesUKCreateRequest:
    carrier: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('carrier') }})
    parameters: CarrierAccountHermesUKCreateRequestParameters = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parameters') }})
    

