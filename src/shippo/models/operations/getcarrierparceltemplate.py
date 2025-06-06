"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from shippo.types import BaseModel
from shippo.utils import FieldMetadata, HeaderMetadata, PathParamMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetCarrierParcelTemplateGlobalsTypedDict(TypedDict):
    shippo_api_version: NotRequired[str]
    r"""Optional string used to pick a non-default API version to use. See our <a href=\"https://docs.goshippo.com/docs/api_concepts/apiversioning/\">API version</a> guide."""


class GetCarrierParcelTemplateGlobals(BaseModel):
    shippo_api_version: Annotated[
        Optional[str],
        pydantic.Field(alias="SHIPPO-API-VERSION"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Optional string used to pick a non-default API version to use. See our <a href=\"https://docs.goshippo.com/docs/api_concepts/apiversioning/\">API version</a> guide."""


class GetCarrierParcelTemplateRequestTypedDict(TypedDict):
    carrier_parcel_template_token: str
    r"""The unique string representation of the carrier parcel template"""


class GetCarrierParcelTemplateRequest(BaseModel):
    carrier_parcel_template_token: Annotated[
        str,
        pydantic.Field(alias="CarrierParcelTemplateToken"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The unique string representation of the carrier parcel template"""
