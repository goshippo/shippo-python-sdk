"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

import requests as requests_http
from .sdkconfiguration import SDKConfiguration
from shippo import utils
from shippo._hooks import AfterErrorContext, AfterSuccessContext, BeforeRequestContext, HookContext
from shippo.models import components, errors, operations
from typing import Optional

class Transactions:
    r"""A transaction is the purchase of a shipping label from a shipping provider for a specific service. You can print purchased labels and used them to ship a parcel with a carrier, such as USPS or FedEx.
    <SchemaDefinition schemaRef=\"#/components/schemas/Transaction\"/>
    """
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def list(self, request: operations.ListTransactionsRequest) -> components.TransactionPaginatedList:
        r"""List all shipping labels
        Returns a list of all transaction objects.
        """
        hook_ctx = HookContext(operation_id='ListTransactions', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        _globals = operations.ListTransactionsGlobals(
            shippo_api_version=self.sdk_configuration.globals.shippo_api_version,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/transactions'
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        headers = { **utils.get_headers(request, _globals), **headers }
        query_params = { **utils.get_query_params(request, _globals), **query_params }
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        try:
            req = client.prepare_request(requests_http.Request('GET', url, params=query_params, headers=headers))
            req = self.sdk_configuration.get_hooks().before_request(BeforeRequestContext(hook_ctx), req)
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), None, e)
            if e is not None:
                raise e

        if utils.match_status_codes(['400','4XX','5XX'], http_res.status_code):
            result, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), http_res, None)
            if e is not None:
                raise e
            if result is not None:
                http_res = result
        else:
            http_res = self.sdk_configuration.get_hooks().after_success(AfterSuccessContext(hook_ctx), http_res)
            
        
        
        
        if http_res.status_code == 200:
            # pylint: disable=no-else-return
            if utils.match_content_type(http_res.headers.get('Content-Type') or '', 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[components.TransactionPaginatedList])
                return out
            
            content_type = http_res.headers.get('Content-Type')
            raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 400 or http_res.status_code >= 400 and http_res.status_code < 500:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

    
    
    def create(self, request: operations.CreateTransactionRequestBody) -> components.Transaction:
        r"""Create a shipping label
        Creates a new transaction object and purchases the shipping label using a rate object that has previously been created. <br> OR <br> Creates a new transaction object and purchases the shipping label instantly using shipment details, an existing carrier account, and an existing service level token.
        """
        hook_ctx = HookContext(operation_id='CreateTransaction', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        _globals = operations.CreateTransactionGlobals(
            shippo_api_version=self.sdk_configuration.globals.shippo_api_version,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/transactions'
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        headers = { **utils.get_headers(request, _globals), **headers }
        req_content_type, data, form = utils.serialize_request_body(request, operations.CreateTransactionRequestBody, "request", False, False, 'json')
        if req_content_type is not None and req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        try:
            req = client.prepare_request(requests_http.Request('POST', url, params=query_params, data=data, files=form, headers=headers))
            req = self.sdk_configuration.get_hooks().before_request(BeforeRequestContext(hook_ctx), req)
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), None, e)
            if e is not None:
                raise e

        if utils.match_status_codes(['400','4XX','5XX'], http_res.status_code):
            result, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), http_res, None)
            if e is not None:
                raise e
            if result is not None:
                http_res = result
        else:
            http_res = self.sdk_configuration.get_hooks().after_success(AfterSuccessContext(hook_ctx), http_res)
            
        
        
        
        if http_res.status_code == 201:
            # pylint: disable=no-else-return
            if utils.match_content_type(http_res.headers.get('Content-Type') or '', 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[components.Transaction])
                return out
            
            content_type = http_res.headers.get('Content-Type')
            raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 400 or http_res.status_code >= 400 and http_res.status_code < 500:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

    
    
    def get(self, transaction_id: str) -> components.Transaction:
        r"""Retrieve a shipping label
        Returns an existing transaction using an object ID.
        """
        hook_ctx = HookContext(operation_id='GetTransaction', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        request = operations.GetTransactionRequest(
            transaction_id=transaction_id,
        )
        
        _globals = operations.GetTransactionGlobals(
            shippo_api_version=self.sdk_configuration.globals.shippo_api_version,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(base_url, '/transactions/{TransactionId}', request, _globals)
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        headers = { **utils.get_headers(request, _globals), **headers }
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        try:
            req = client.prepare_request(requests_http.Request('GET', url, params=query_params, headers=headers))
            req = self.sdk_configuration.get_hooks().before_request(BeforeRequestContext(hook_ctx), req)
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), None, e)
            if e is not None:
                raise e

        if utils.match_status_codes(['400','4XX','5XX'], http_res.status_code):
            result, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), http_res, None)
            if e is not None:
                raise e
            if result is not None:
                http_res = result
        else:
            http_res = self.sdk_configuration.get_hooks().after_success(AfterSuccessContext(hook_ctx), http_res)
            
        
        
        
        if http_res.status_code == 200:
            # pylint: disable=no-else-return
            if utils.match_content_type(http_res.headers.get('Content-Type') or '', 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[components.Transaction])
                return out
            
            content_type = http_res.headers.get('Content-Type')
            raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 400 or http_res.status_code >= 400 and http_res.status_code < 500:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

    

