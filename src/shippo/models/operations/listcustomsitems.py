"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from shippo.types import BaseModel
from shippo.utils import FieldMetadata, HeaderMetadata, QueryParamMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ListCustomsItemsGlobalsTypedDict(TypedDict):
    shippo_api_version: NotRequired[str]
    r"""String used to pick a non-default API version to use"""
    

class ListCustomsItemsGlobals(BaseModel):
    shippo_api_version: Annotated[Optional[str], pydantic.Field(alias="SHIPPO-API-VERSION"), FieldMetadata(header=HeaderMetadata(style="simple", explode=False))] = None
    r"""String used to pick a non-default API version to use"""
    

class ListCustomsItemsRequestTypedDict(TypedDict):
    page: NotRequired[int]
    r"""The page number you want to select"""
    results: NotRequired[int]
    r"""The number of results to return per page (max 100)"""
    

class ListCustomsItemsRequest(BaseModel):
    page: Annotated[Optional[int], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = 1
    r"""The page number you want to select"""
    results: Annotated[Optional[int], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = 25
    r"""The number of results to return per page (max 100)"""
    
