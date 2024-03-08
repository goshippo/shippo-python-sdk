"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import ratelistwrapper as components_ratelistwrapper
from typing import Optional


@dataclasses.dataclass
class ListShipmentRatesByCurrencyCodeRequest:
    shipment_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ShipmentId', 'style': 'simple', 'explode': False }})
    r"""Object ID of the shipment to update"""
    currency_code: str = dataclasses.field(default='USD', metadata={'path_param': { 'field_name': 'CurrencyCode', 'style': 'simple', 'explode': False }})
    r"""ISO currency code for the rates"""
    page: Optional[int] = dataclasses.field(default=1, metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    r"""The page number you want to select"""
    results: Optional[int] = dataclasses.field(default=25, metadata={'query_param': { 'field_name': 'results', 'style': 'form', 'explode': True }})
    r"""The number of results to return per page (max 100)"""
    shippo_api_version: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'SHIPPO-API-VERSION', 'style': 'simple', 'explode': False }})
    r"""String used to pick a non-default API version to use"""
    



@dataclasses.dataclass
class ListShipmentRatesByCurrencyCodeResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    rate_list_wrapper: Optional[components_ratelistwrapper.RateListWrapper] = dataclasses.field(default=None)
    

