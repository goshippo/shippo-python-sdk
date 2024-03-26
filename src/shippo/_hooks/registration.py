from typing import Union, Tuple

import requests

from .types import Hooks, BeforeRequestHook, BeforeRequestContext, SDKInitHook


# This file is only ever generated once on the first generation and then is free to be modified.
# Any hooks you wish to add should be registered in the init_hooks function. Feel free to define them
# in this file or in separate files in the hooks folder.


def add_shippo_token_to_auth_header_if_missing(request: requests.PreparedRequest):
    auth_header = request.headers.get("authorization")
    if auth_header is not None and auth_header.startswith("ShippoToken") is False:
        request.headers["authorization"] = f"ShippoToken {auth_header}"


class ShippoAuthBeforeRequestHook(BeforeRequestHook):

    def before_request(
            self, hook_ctx: BeforeRequestContext, request: requests.PreparedRequest
    ) -> Union[requests.PreparedRequest, Exception]:
        add_shippo_token_to_auth_header_if_missing(request)
        return request


class ShippoAuthTokenInitHook(SDKInitHook):

    def sdk_init(self, base_url: str, client: requests.Session) -> Tuple[str, requests.Session]:
        send_delegate = client.send

        def custom_send(request, **kwargs):
            add_shippo_token_to_auth_header_if_missing(request)
            return send_delegate(request, **kwargs)

        client.send = custom_send
        return base_url, client


def init_hooks(hooks: Hooks):
    # pylint: disable=unused-argument
    """Add hooks by calling hooks.register{sdk_init/before_request/after_success/after_error}Hook 
    with an instance of a hook that implements that specific Hook interface
    Hooks are registered per SDK instance, and are valid for the lifetime of the SDK instance"""
    hooks.register_sdk_init_hook(ShippoAuthTokenInitHook())
