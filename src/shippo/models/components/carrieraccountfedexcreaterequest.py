"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from pydantic.functional_validators import AfterValidator
from shippo.types import BaseModel
from shippo.utils import validate_const
from typing import Literal
from typing_extensions import Annotated, TypedDict


class CarrierAccountFedExCreateRequestParametersTypedDict(TypedDict):
    pass


class CarrierAccountFedExCreateRequestParameters(BaseModel):
    pass


class CarrierAccountFedExCreateRequestTypedDict(TypedDict):
    parameters: CarrierAccountFedExCreateRequestParametersTypedDict
    carrier: Literal["fedex"]


class CarrierAccountFedExCreateRequest(BaseModel):
    parameters: CarrierAccountFedExCreateRequestParameters

    CARRIER: Annotated[
        Annotated[Literal["fedex"], AfterValidator(validate_const("fedex"))],
        pydantic.Field(alias="carrier"),
    ] = "fedex"
