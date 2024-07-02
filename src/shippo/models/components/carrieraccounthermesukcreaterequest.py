"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from shippo.types import BaseModel
from typing import TypedDict


class CarrierAccountHermesUKCreateRequestParametersTypedDict(TypedDict):
    pass
    

class CarrierAccountHermesUKCreateRequestParameters(BaseModel):
    pass
    

class CarrierAccountHermesUKCreateRequestTypedDict(TypedDict):
    carrier: str
    parameters: CarrierAccountHermesUKCreateRequestParametersTypedDict
    

class CarrierAccountHermesUKCreateRequest(BaseModel):
    carrier: str
    parameters: CarrierAccountHermesUKCreateRequestParameters
    
