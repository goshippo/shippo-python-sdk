"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from shippo.types import BaseModel
from typing_extensions import TypedDict


class TrackingStatusSubstatusTypedDict(TypedDict):
    r"""A finer-grained classification of the tracking event."""

    code: str
    r"""A code that represents the substatus of the shipment. See the <a href=\"https://docs.goshippo.com/docs/tracking/tracking/#event-definitions\">Event Definitions</a> for more information."""
    text: str
    r"""A human-readable description of the substatus. See the <a href=\"https://docs.goshippo.com/docs/tracking/tracking/#event-definitions\">Event Definitions</a> for more information."""
    action_required: bool
    r"""Indicates whether the substatus requires action from the shipper or recipient to complete delivery."""


class TrackingStatusSubstatus(BaseModel):
    r"""A finer-grained classification of the tracking event."""

    code: str
    r"""A code that represents the substatus of the shipment. See the <a href=\"https://docs.goshippo.com/docs/tracking/tracking/#event-definitions\">Event Definitions</a> for more information."""

    text: str
    r"""A human-readable description of the substatus. See the <a href=\"https://docs.goshippo.com/docs/tracking/tracking/#event-definitions\">Event Definitions</a> for more information."""

    action_required: bool
    r"""Indicates whether the substatus requires action from the shipper or recipient to complete delivery."""
