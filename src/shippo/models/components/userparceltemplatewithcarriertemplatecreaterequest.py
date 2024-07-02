"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from .weightunitenum import WeightUnitEnum
from shippo.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class UserParcelTemplateWithCarrierTemplateCreateRequestTypedDict(TypedDict):
    template: NotRequired[str]
    r"""The object representing the carrier parcel template"""
    weight: NotRequired[str]
    r"""The weight of the package, in units specified by the weight_unit attribute."""
    weight_unit: NotRequired[WeightUnitEnum]
    r"""The unit used for weight."""
    

class UserParcelTemplateWithCarrierTemplateCreateRequest(BaseModel):
    template: Optional[str] = None
    r"""The object representing the carrier parcel template"""
    weight: Optional[str] = None
    r"""The weight of the package, in units specified by the weight_unit attribute."""
    weight_unit: Optional[WeightUnitEnum] = None
    r"""The unit used for weight."""
    
