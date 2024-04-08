"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import instanttransactionrequestbody as components_instanttransactionrequestbody
from ...models.components import transactioncreaterequest as components_transactioncreaterequest
from typing import Optional, Union


@dataclasses.dataclass
class CreateTransactionGlobals:
    shippo_api_version: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'SHIPPO-API-VERSION', 'style': 'simple', 'explode': False }})
    r"""String used to pick a non-default API version to use"""
    



@dataclasses.dataclass
class CreateTransactionRequest:
    shippo_api_version: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'SHIPPO-API-VERSION', 'style': 'simple', 'explode': False }})
    r"""String used to pick a non-default API version to use"""
    request_body: Optional[Union[components_transactioncreaterequest.TransactionCreateRequest, components_instanttransactionrequestbody.InstantTransactionRequestBody]] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""Examples."""
    

