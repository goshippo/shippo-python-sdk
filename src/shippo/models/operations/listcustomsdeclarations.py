"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from typing import Optional


@dataclasses.dataclass
class ListCustomsDeclarationsGlobals:
    shippo_api_version: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'SHIPPO-API-VERSION', 'style': 'simple', 'explode': False }})
    r"""Optional string used to pick a non-default API version to use. See our <a href=\\"https://docs.goshippo.com/docs/api_concepts/apiversioning/\\">API version</a> guide."""
    



@dataclasses.dataclass
class ListCustomsDeclarationsRequest:
    page: Optional[int] = dataclasses.field(default=1, metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    r"""The page number you want to select"""
    results: Optional[int] = dataclasses.field(default=5, metadata={'query_param': { 'field_name': 'results', 'style': 'form', 'explode': True }})
    r"""The number of results to return per page (max 100, default 5)"""
    

