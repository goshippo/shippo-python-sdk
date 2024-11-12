"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from typing import Optional


@dataclasses.dataclass
class GetOrderGlobals:
    shippo_api_version: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'SHIPPO-API-VERSION', 'style': 'simple', 'explode': False }})
    r"""Optional string used to pick a non-default API version to use. See our <a href=\\"https://docs.goshippo.com/docs/api_concepts/apiversioning/\\">API version</a> guide."""
    



@dataclasses.dataclass
class GetOrderRequest:
    order_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'OrderId', 'style': 'simple', 'explode': False }})
    r"""Object ID of the order"""
    

