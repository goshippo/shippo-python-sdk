"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import webhookupdaterequest as components_webhookupdaterequest


@dataclasses.dataclass
class UpdateWebhookRequest:
    webhook_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'webhookId', 'style': 'simple', 'explode': False }})
    r"""Object ID of the webhook to retrieve"""
    webhook_update_request: components_webhookupdaterequest.WebhookUpdateRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

