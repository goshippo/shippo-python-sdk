"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class OrderStatusEnum(str, Enum):
    r"""Current state of the order. See the <a href=\"https://docs.goshippo.com/docs/orders/orders/\">orders tutorial</a>
    for the logic of how the status is handled.
    """

    UNKNOWN = "UNKNOWN"
    AWAITPAY = "AWAITPAY"
    PAID = "PAID"
    REFUNDED = "REFUNDED"
    CANCELLED = "CANCELLED"
    PARTIALLY_FULFILLED = "PARTIALLY_FULFILLED"
    SHIPPED = "SHIPPED"
