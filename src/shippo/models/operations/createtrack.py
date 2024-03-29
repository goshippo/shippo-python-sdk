"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import tracksrequest as components_tracksrequest
from typing import Optional


@dataclasses.dataclass
class CreateTrackRequest:
    shippo_api_version: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'SHIPPO-API-VERSION', 'style': 'simple', 'explode': False }})
    r"""String used to pick a non-default API version to use"""
    tracks_request: Optional[components_tracksrequest.TracksRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

