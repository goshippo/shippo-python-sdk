"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import defaultparceltemplateupdaterequest as components_defaultparceltemplateupdaterequest
from typing import Optional


@dataclasses.dataclass
class UpdateDefaultParcelTemplateRequest:
    shippo_api_version: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'SHIPPO-API-VERSION', 'style': 'simple', 'explode': False }})
    r"""String used to pick a non-default API version to use"""
    default_parcel_template_update_request: Optional[components_defaultparceltemplateupdaterequest.DefaultParcelTemplateUpdateRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

