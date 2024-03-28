"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import userparceltemplate as components_userparceltemplate
from typing import List, Optional


@dataclasses.dataclass
class ListUserParcelTemplatesRequest:
    shippo_api_version: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'SHIPPO-API-VERSION', 'style': 'simple', 'explode': False }})
    r"""String used to pick a non-default API version to use"""
    



@dataclasses.dataclass
class ListUserParcelTemplatesResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    user_parcel_template_list_response: Optional[List[components_userparceltemplate.UserParcelTemplate]] = dataclasses.field(default=None)
    

