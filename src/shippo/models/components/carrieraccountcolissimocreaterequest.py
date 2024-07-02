"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from shippo.types import BaseModel
from typing import TypedDict


class CarrierAccountColissimoCreateRequestParametersTypedDict(TypedDict):
    pass
    

class CarrierAccountColissimoCreateRequestParameters(BaseModel):
    pass
    

class CarrierAccountColissimoCreateRequestTypedDict(TypedDict):
    carrier: str
    parameters: CarrierAccountColissimoCreateRequestParametersTypedDict
    

class CarrierAccountColissimoCreateRequest(BaseModel):
    carrier: str
    parameters: CarrierAccountColissimoCreateRequestParameters
    
