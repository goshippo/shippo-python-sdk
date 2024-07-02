"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from shippo.types import BaseModel
from shippo.utils import FieldMetadata, HeaderMetadata, PathParamMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GetTransactionGlobalsTypedDict(TypedDict):
    shippo_api_version: NotRequired[str]
    r"""String used to pick a non-default API version to use"""
    

class GetTransactionGlobals(BaseModel):
    shippo_api_version: Annotated[Optional[str], pydantic.Field(alias="SHIPPO-API-VERSION"), FieldMetadata(header=HeaderMetadata(style="simple", explode=False))] = None
    r"""String used to pick a non-default API version to use"""
    

class GetTransactionRequestTypedDict(TypedDict):
    transaction_id: str
    r"""Object ID of the transaction to update"""
    

class GetTransactionRequest(BaseModel):
    transaction_id: Annotated[str, pydantic.Field(alias="TransactionId"), FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""Object ID of the transaction to update"""
    
