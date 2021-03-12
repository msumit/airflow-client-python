# coding: utf-8

"""
    Airflow API (Stable)

    # Overview  To facilitate management, Apache Airflow supports a range of REST API endpoints across its objects. This section provides an overview of the API design, methods, and supported use cases.  Most of the endpoints accept `JSON` as input and return `JSON` responses. This means that you must usually add the following headers to your request: ``` Content-type: application/json Accept: application/json ```  ## Resources  The term `resource` refers to a single type of object in the Airflow metadata. An API is broken up by its endpoint's corresponding resource. The name of a resource is typically plural and expressed in camelCase. Example: `dagRuns`.  Resource names are used as part of endpoint URLs, as well as in API parameters and responses.  ## CRUD Operations  The platform supports **C**reate, **R**ead, **U**pdate, and **D**elete operations on most resources. You can review the standards for these operations and their standard parameters below.  Some endpoints have special behavior as exceptions.  ### Create  To create a resource, you typically submit an HTTP `POST` request with the resource's required metadata in the request body. The response returns a `201 Created` response code upon success with the resource's metadata, including its internal `id`, in the response body.  ### Read  The HTTP `GET` request can be used to read a resource or to list a number of resources.  A resource's `id` can be submitted in the request parameters to read a specific resource. The response usually returns a `200 OK` response code upon success, with the resource's metadata in the response body.  If a `GET` request does not include a specific resource `id`, it is treated as a list request. The response usually returns a `200 OK` response code upon success, with an object containing a list of resources' metadata in the response body.  When reading resources, some common query parameters are usually available. e.g.: ``` v1/connections?limit=25&offset=25 ```  |Query Parameter|Type|Description| |---------------|----|-----------| |limit|integer|Maximum number of objects to fetch. Usually 25 by default| |offset|integer|Offset after which to start returning objects. For use with limit query parameter.|  ### Update  Updating a resource requires the resource `id`, and is typically done using an HTTP `PATCH` request, with the fields to modify in the request body. The response usually returns a `200 OK` response code upon success, with information about the modified resource in the response body.  ### Delete  Deleting a resource requires the resource `id` and is typically executing via an HTTP `DELETE` request. The response usually returns a `204 No Content` response code upon success.  ## Conventions  - Resource names are plural and expressed in camelCase. - Names are consistent between URL parameter name and field name.  - Field names are in snake_case. ```json {     \"name\": \"string\",     \"slots\": 0,     \"occupied_slots\": 0,     \"used_slots\": 0,     \"queued_slots\": 0,     \"open_slots\": 0 } ```  ### Update Mask  Update mask is available as a query parameter in patch endpoints. It is used to notify the API which fields you want to update. Using `update_mask` makes it easier to update objects by helping the server know which fields to update in an object instead of updating all fields. The update request ignores any fields that aren't specified in the field mask, leaving them with their current values.  Example: ```   resource = request.get('/resource/my-id').json()   resource['my_field'] = 'new-value'   request.patch('/resource/my-id?update_mask=my_field', data=json.dumps(resource)) ```  ## Versioning and Endpoint Lifecycle  - API versioning is not synchronized to specific releases of the Apache Airflow. - APIs are designed to be backward compatible. - Any changes to the API will first go through a deprecation phase.  # Summary of Changes  | Airflow version | Description | |-|-| | v2.0 | Initial release | | v2.0.2    | Added /plugins endpoint |  # Trying the API  You can use a third party client, such as [curl](https://curl.haxx.se/), [HTTPie](https://httpie.org/), [Postman](https://www.postman.com/) or [the Insomnia rest client](https://insomnia.rest/) to test the Apache Airflow API.  Note that you will need to pass credentials data.  For e.g., here is how to pause a DAG with [curl](https://curl.haxx.se/), when basic authorization is used: ```bash curl -X POST 'https://example.com/api/v1/dags/{dag_id}?update_mask=is_paused' \\ -H 'Content-Type: application/json' \\ --user \"username:password\" \\ -d '{     \"is_paused\": true }' ```  Using a graphical tool such as [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/), it is possible to import the API specifications directly:  1. Download the API specification by clicking the **Download** button at top of this document 2. Import the JSON specification in the graphical tool of your choice.   - In *Postman*, you can click the **import** button at the top   - With *Insomnia*, you can just drag-and-drop the file on the UI  Note that with *Postman*, you can also generate code snippets by selecting a request and clicking on the **Code** button.  ## Enabling CORS  [Cross-origin resource sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) is a browser security feature that restricts HTTP requests that are initiated from scripts running in the browser.  For details on enabling/configuring CORS, see [Enabling CORS](https://airflow.apache.org/docs/apache-airflow/stable/security/api.html).  # Authentication  To be able to meet the requirements of many organizations, Airflow supports many authentication methods, and it is even possible to add your own method.  If you want to check which auth backend is currently set, you can use `airflow config get-value api auth_backend` command as in the example below. ```bash $ airflow config get-value api auth_backend airflow.api.auth.backend.basic_auth ``` The default is to deny all requests.  For details on configuring the authentication, see [API Authorization](https://airflow.apache.org/docs/apache-airflow/stable/security/api.html).  # Errors  We follow the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs. As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Unauthenticated  This indicates that the request has not been applied because it lacks valid authentication credentials for the target resource. Please check that you have valid credentials.  ## PermissionDenied  This response means that the server understood the request but refuses to authorize it because it lacks sufficient rights to the resource. It happens when you do not have the necessary permission to execute the action you performed. You need to get the appropriate permissions in other to resolve this error.  ## BadRequest  This response means that the server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). To resolve this, please ensure that your syntax is correct.  ## NotFound  This client error response indicates that the server cannot find the requested resource.  ## MethodNotAllowed  Indicates that the request method is known by the server but is not supported by the target resource.  ## NotAcceptable  The target resource does not have a current representation that would be acceptable to the user agent, according to the proactive negotiation header fields received in the request, and the server is unwilling to supply a default representation.  ## AlreadyExists  The request could not be completed due to a conflict with the current state of the target resource, meaning that the resource already exists  ## Unknown  This means that the server encountered an unexpected condition that prevented it from fulfilling the request.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: dev@airflow.apache.org
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from airflow-client.api_client import ApiClient
from airflow-client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class DAGRunApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_dag_run(self, dag_id, dag_run_id, **kwargs):  # noqa: E501
        """Delete a DAG run  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_dag_run(dag_id, dag_run_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str dag_id: The DAG ID. (required)
        :param str dag_run_id: The DAG run ID. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_dag_run_with_http_info(dag_id, dag_run_id, **kwargs)  # noqa: E501

    def delete_dag_run_with_http_info(self, dag_id, dag_run_id, **kwargs):  # noqa: E501
        """Delete a DAG run  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_dag_run_with_http_info(dag_id, dag_run_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str dag_id: The DAG ID. (required)
        :param str dag_run_id: The DAG run ID. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'dag_id',
            'dag_run_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_dag_run" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'dag_id' is set
        if self.api_client.client_side_validation and ('dag_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['dag_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `dag_id` when calling `delete_dag_run`")  # noqa: E501
        # verify the required parameter 'dag_run_id' is set
        if self.api_client.client_side_validation and ('dag_run_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['dag_run_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `dag_run_id` when calling `delete_dag_run`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dag_id' in local_var_params:
            path_params['dag_id'] = local_var_params['dag_id']  # noqa: E501
        if 'dag_run_id' in local_var_params:
            path_params['dag_run_id'] = local_var_params['dag_run_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'GoogleOpenId', 'Kerberos']  # noqa: E501

        return self.api_client.call_api(
            '/dags/{dag_id}/dagRuns/{dag_run_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dag_run(self, dag_id, dag_run_id, **kwargs):  # noqa: E501
        """Get a DAG run  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dag_run(dag_id, dag_run_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str dag_id: The DAG ID. (required)
        :param str dag_run_id: The DAG run ID. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: DAGRun
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_dag_run_with_http_info(dag_id, dag_run_id, **kwargs)  # noqa: E501

    def get_dag_run_with_http_info(self, dag_id, dag_run_id, **kwargs):  # noqa: E501
        """Get a DAG run  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dag_run_with_http_info(dag_id, dag_run_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str dag_id: The DAG ID. (required)
        :param str dag_run_id: The DAG run ID. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(DAGRun, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'dag_id',
            'dag_run_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dag_run" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'dag_id' is set
        if self.api_client.client_side_validation and ('dag_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['dag_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `dag_id` when calling `get_dag_run`")  # noqa: E501
        # verify the required parameter 'dag_run_id' is set
        if self.api_client.client_side_validation and ('dag_run_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['dag_run_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `dag_run_id` when calling `get_dag_run`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dag_id' in local_var_params:
            path_params['dag_id'] = local_var_params['dag_id']  # noqa: E501
        if 'dag_run_id' in local_var_params:
            path_params['dag_run_id'] = local_var_params['dag_run_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'GoogleOpenId', 'Kerberos']  # noqa: E501

        return self.api_client.call_api(
            '/dags/{dag_id}/dagRuns/{dag_run_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DAGRun',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dag_runs(self, dag_id, **kwargs):  # noqa: E501
        """List DAG runs  # noqa: E501

        This endpoint allows specifying `~` as the dag_id to retrieve DAG runs for all DAGs.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dag_runs(dag_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str dag_id: The DAG ID. (required)
        :param int limit: The numbers of items to return.
        :param int offset: The number of items to skip before starting to collect the result set.
        :param datetime execution_date_gte: Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte parameter to receive only the selected period. 
        :param datetime execution_date_lte: Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte parameter to receive only the selected period. 
        :param datetime start_date_gte: Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period. 
        :param datetime start_date_lte: Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period. 
        :param datetime end_date_gte: Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period. 
        :param datetime end_date_lte: Returns objects less than or equal to the specified date.  This can be combined with start_date_gte parameter to receive only the selected period. 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: DAGRunCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_dag_runs_with_http_info(dag_id, **kwargs)  # noqa: E501

    def get_dag_runs_with_http_info(self, dag_id, **kwargs):  # noqa: E501
        """List DAG runs  # noqa: E501

        This endpoint allows specifying `~` as the dag_id to retrieve DAG runs for all DAGs.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dag_runs_with_http_info(dag_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str dag_id: The DAG ID. (required)
        :param int limit: The numbers of items to return.
        :param int offset: The number of items to skip before starting to collect the result set.
        :param datetime execution_date_gte: Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte parameter to receive only the selected period. 
        :param datetime execution_date_lte: Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte parameter to receive only the selected period. 
        :param datetime start_date_gte: Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period. 
        :param datetime start_date_lte: Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period. 
        :param datetime end_date_gte: Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period. 
        :param datetime end_date_lte: Returns objects less than or equal to the specified date.  This can be combined with start_date_gte parameter to receive only the selected period. 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(DAGRunCollection, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'dag_id',
            'limit',
            'offset',
            'execution_date_gte',
            'execution_date_lte',
            'start_date_gte',
            'start_date_lte',
            'end_date_gte',
            'end_date_lte'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dag_runs" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'dag_id' is set
        if self.api_client.client_side_validation and ('dag_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['dag_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `dag_id` when calling `get_dag_runs`")  # noqa: E501

        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `get_dag_runs`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'dag_id' in local_var_params:
            path_params['dag_id'] = local_var_params['dag_id']  # noqa: E501

        query_params = []
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'execution_date_gte' in local_var_params and local_var_params['execution_date_gte'] is not None:  # noqa: E501
            query_params.append(('execution_date_gte', local_var_params['execution_date_gte']))  # noqa: E501
        if 'execution_date_lte' in local_var_params and local_var_params['execution_date_lte'] is not None:  # noqa: E501
            query_params.append(('execution_date_lte', local_var_params['execution_date_lte']))  # noqa: E501
        if 'start_date_gte' in local_var_params and local_var_params['start_date_gte'] is not None:  # noqa: E501
            query_params.append(('start_date_gte', local_var_params['start_date_gte']))  # noqa: E501
        if 'start_date_lte' in local_var_params and local_var_params['start_date_lte'] is not None:  # noqa: E501
            query_params.append(('start_date_lte', local_var_params['start_date_lte']))  # noqa: E501
        if 'end_date_gte' in local_var_params and local_var_params['end_date_gte'] is not None:  # noqa: E501
            query_params.append(('end_date_gte', local_var_params['end_date_gte']))  # noqa: E501
        if 'end_date_lte' in local_var_params and local_var_params['end_date_lte'] is not None:  # noqa: E501
            query_params.append(('end_date_lte', local_var_params['end_date_lte']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'GoogleOpenId', 'Kerberos']  # noqa: E501

        return self.api_client.call_api(
            '/dags/{dag_id}/dagRuns', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DAGRunCollection',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dag_runs_batch(self, list_dag_runs_form, **kwargs):  # noqa: E501
        """List DAG runs (batch)  # noqa: E501

        This endpoint is a POST to allow filtering across a large number of DAG IDs, where as a GET it would run in to maximum HTTP request URL length limit.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dag_runs_batch(list_dag_runs_form, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param ListDagRunsForm list_dag_runs_form: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: DAGRunCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_dag_runs_batch_with_http_info(list_dag_runs_form, **kwargs)  # noqa: E501

    def get_dag_runs_batch_with_http_info(self, list_dag_runs_form, **kwargs):  # noqa: E501
        """List DAG runs (batch)  # noqa: E501

        This endpoint is a POST to allow filtering across a large number of DAG IDs, where as a GET it would run in to maximum HTTP request URL length limit.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dag_runs_batch_with_http_info(list_dag_runs_form, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param ListDagRunsForm list_dag_runs_form: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(DAGRunCollection, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'list_dag_runs_form'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dag_runs_batch" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'list_dag_runs_form' is set
        if self.api_client.client_side_validation and ('list_dag_runs_form' not in local_var_params or  # noqa: E501
                                                        local_var_params['list_dag_runs_form'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `list_dag_runs_form` when calling `get_dag_runs_batch`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'list_dag_runs_form' in local_var_params:
            body_params = local_var_params['list_dag_runs_form']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'GoogleOpenId', 'Kerberos']  # noqa: E501

        return self.api_client.call_api(
            '/dags/~/dagRuns/list', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DAGRunCollection',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_dag_run(self, dag_id, dag_run, **kwargs):  # noqa: E501
        """Trigger a new DAG run  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_dag_run(dag_id, dag_run, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str dag_id: The DAG ID. (required)
        :param DAGRun dag_run: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: DAGRun
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.post_dag_run_with_http_info(dag_id, dag_run, **kwargs)  # noqa: E501

    def post_dag_run_with_http_info(self, dag_id, dag_run, **kwargs):  # noqa: E501
        """Trigger a new DAG run  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_dag_run_with_http_info(dag_id, dag_run, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str dag_id: The DAG ID. (required)
        :param DAGRun dag_run: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(DAGRun, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'dag_id',
            'dag_run'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_dag_run" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'dag_id' is set
        if self.api_client.client_side_validation and ('dag_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['dag_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `dag_id` when calling `post_dag_run`")  # noqa: E501
        # verify the required parameter 'dag_run' is set
        if self.api_client.client_side_validation and ('dag_run' not in local_var_params or  # noqa: E501
                                                        local_var_params['dag_run'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `dag_run` when calling `post_dag_run`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dag_id' in local_var_params:
            path_params['dag_id'] = local_var_params['dag_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'dag_run' in local_var_params:
            body_params = local_var_params['dag_run']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'GoogleOpenId', 'Kerberos']  # noqa: E501

        return self.api_client.call_api(
            '/dags/{dag_id}/dagRuns', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DAGRun',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
