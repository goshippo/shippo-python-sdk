"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from shippo.types import BaseModel
from shippo.utils import FieldMetadata, PathParamMetadata
from typing_extensions import Annotated, TypedDict


class GetWebhookRequestTypedDict(TypedDict):
    webhook_id: str
    r"""Object ID of the webhook to retrieve"""


class GetWebhookRequest(BaseModel):
    webhook_id: Annotated[
        str,
        pydantic.Field(alias="webhookId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Object ID of the webhook to retrieve"""
