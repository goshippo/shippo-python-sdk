"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import shippoaccount as components_shippoaccount
from typing import Optional


@dataclasses.dataclass
class GetShippoAccountRequest:
    shippo_account_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ShippoAccountId', 'style': 'simple', 'explode': False }})
    r"""Object ID of the ShippoAccount"""
    shippo_api_version: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'SHIPPO-API-VERSION', 'style': 'simple', 'explode': False }})
    r"""String used to pick a non-default API version to use"""
    



@dataclasses.dataclass
class GetShippoAccountResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    shippo_account: Optional[components_shippoaccount.ShippoAccount] = dataclasses.field(default=None)
    

