"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from typing import Optional


@dataclasses.dataclass
class CreateShippoAccountGlobals:
    shippo_api_version: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'SHIPPO-API-VERSION', 'style': 'simple', 'explode': False }})
    r"""Optional string used to pick a non-default API version to use. See our <a href=\\"https://docs.goshippo.com/docs/api_concepts/apiversioning/\\">API version</a> guide."""
    

