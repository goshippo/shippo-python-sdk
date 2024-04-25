from typing import Union, Tuple

import json
import requests

from .types import Hooks, BeforeRequestHook, BeforeRequestContext, SDKInitHook, AfterSuccessHook, AfterSuccessContext


# This file is only ever generated once on the first generation and then is free to be modified.
# Any hooks you wish to add should be registered in the init_hooks function. Feel free to define them
# in this file or in separate files in the hooks folder.


def add_shippo_token_to_auth_header_if_missing(request: requests.PreparedRequest):
    auth_header = request.headers.get("authorization")
    if auth_header is not None and auth_header.startswith("shippo_"):
        request.headers["authorization"] = f"ShippoToken {auth_header}"


class ShippoAuthBeforeRequestHook(BeforeRequestHook):

    def before_request(
            self, hook_ctx: BeforeRequestContext, request: requests.PreparedRequest
    ) -> Union[requests.PreparedRequest, Exception]:
        add_shippo_token_to_auth_header_if_missing(request)
        return request


class TransactionCreateResponseAddDiscriminatorAfterSuccessHook(AfterSuccessHook):

    def after_success(self, hook_ctx: AfterSuccessContext, response: requests.Response) -> Union[requests.Response, Exception]:
        if hook_ctx.operation_id == "CreateTransaction":
            if response.status_code == 201:
                content: dict = response.json()
                rate = content.get("rate")
                response_type = None
                if isinstance(rate, str):
                    response_type = "standard"
                elif isinstance(rate, dict):
                    response_type = "instant"
                if response_type is not None:
                    content["responseType"] = response_type
                    updated_content = json.dumps(content)
                    response._content = updated_content.encode(response.encoding)  # pylint: disable=protected-access
        return response

def init_hooks(hooks: Hooks):
    # pylint: disable=unused-argument
    """Add hooks by calling hooks.register{sdk_init/before_request/after_success/after_error}Hook 
    with an instance of a hook that implements that specific Hook interface
    Hooks are registered per SDK instance, and are valid for the lifetime of the SDK instance"""
    hooks.register_before_request_hook(ShippoAuthBeforeRequestHook())
    hooks.register_after_success_hook(TransactionCreateResponseAddDiscriminatorAfterSuccessHook())
