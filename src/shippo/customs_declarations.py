"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .sdkconfiguration import SDKConfiguration
from shippo import utils
from shippo._hooks import AfterErrorContext, AfterSuccessContext, BeforeRequestContext, HookContext
from shippo.models import components, errors, operations
from typing import Optional

class CustomsDeclarations:
    r"""Customs declarations are relevant information, including one or multiple customs items, you need to provide for
    customs clearance for your international shipments.
    <SchemaDefinition schemaRef=\"#/components/schemas/CustomsDeclaration\"/>
    """
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def list(self, page: Optional[int] = None, results: Optional[int] = None, shippo_api_version: Optional[str] = None) -> components.CustomsDeclarationPaginatedList:
        r"""List all customs declarations
        Returns a a list of all customs declaration objects
        """
        hook_ctx = HookContext(operation_id='ListCustomsDeclarations', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        request = operations.ListCustomsDeclarationsRequest(
            page=page,
            results=results,
            shippo_api_version=shippo_api_version,
        )
        
        _globals = operations.ListCustomsDeclarationsGlobals(
            shippo_api_version=self.sdk_configuration.globals.shippo_api_version,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(base_url, '/customs/declarations', request, _globals)
        
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

        if utils.match_status_codes(['4XX','5XX'], http_res.status_code):
            result, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), http_res, None)
            if e is not None:
                raise e
            if result is not None:
                http_res = result
        else:
            http_res = self.sdk_configuration.get_hooks().after_success(AfterSuccessContext(hook_ctx), http_res)
            
        
        
        
        if http_res.status_code == 200:
            if utils.match_content_type(http_res.headers.get('Content-Type') or '', 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[components.CustomsDeclarationPaginatedList])
                return out
            
            content_type = http_res.headers.get('Content-Type')
            raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

    
    
    def create(self, shippo_api_version: Optional[str] = None, customs_declaration_create_request: Optional[components.CustomsDeclarationCreateRequest] = None) -> components.CustomsDeclaration:
        r"""Create a new customs declaration
        Creates a new customs declaration object
        """
        hook_ctx = HookContext(operation_id='CreateCustomsDeclaration', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        request = operations.CreateCustomsDeclarationRequest(
            shippo_api_version=shippo_api_version,
            customs_declaration_create_request=customs_declaration_create_request,
        )
        
        _globals = operations.CreateCustomsDeclarationGlobals(
            shippo_api_version=self.sdk_configuration.globals.shippo_api_version,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(base_url, '/customs/declarations', request, _globals)
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        headers = { **utils.get_headers(request, _globals), **headers }
        req_content_type, data, form = utils.serialize_request_body(request, operations.CreateCustomsDeclarationRequest, "customs_declaration_create_request", False, True, 'json')
        if req_content_type is not None and req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = { **utils.get_query_params(request, _globals), **query_params }
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

        if utils.match_status_codes(['4XX','5XX'], http_res.status_code):
            result, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), http_res, None)
            if e is not None:
                raise e
            if result is not None:
                http_res = result
        else:
            http_res = self.sdk_configuration.get_hooks().after_success(AfterSuccessContext(hook_ctx), http_res)
            
        
        
        
        if http_res.status_code == 201:
            if utils.match_content_type(http_res.headers.get('Content-Type') or '', 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[components.CustomsDeclaration])
                return out
            
            content_type = http_res.headers.get('Content-Type')
            raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

    
    
    def get(self, customs_declaration_id: str, page: Optional[int] = None, shippo_api_version: Optional[str] = None) -> components.CustomsDeclaration:
        r"""Retrieve a customs declaration
        Returns an existing customs declaration using an object ID
        """
        hook_ctx = HookContext(operation_id='GetCustomsDeclaration', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        request = operations.GetCustomsDeclarationRequest(
            customs_declaration_id=customs_declaration_id,
            page=page,
            shippo_api_version=shippo_api_version,
        )
        
        _globals = operations.GetCustomsDeclarationGlobals(
            shippo_api_version=self.sdk_configuration.globals.shippo_api_version,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(base_url, '/customs/declarations/{CustomsDeclarationId}', request, _globals)
        
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

        if utils.match_status_codes(['4XX','5XX'], http_res.status_code):
            result, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), http_res, None)
            if e is not None:
                raise e
            if result is not None:
                http_res = result
        else:
            http_res = self.sdk_configuration.get_hooks().after_success(AfterSuccessContext(hook_ctx), http_res)
            
        
        
        
        if http_res.status_code == 200:
            if utils.match_content_type(http_res.headers.get('Content-Type') or '', 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[components.CustomsDeclaration])
                return out
            
            content_type = http_res.headers.get('Content-Type')
            raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

    

