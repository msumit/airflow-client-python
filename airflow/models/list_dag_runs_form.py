# coding: utf-8

"""
    Airflow API (Stable)

    # Overview  To facilitate management, Apache Airflow supports a range of REST API endpoints across its objects. This section provides an overview of the API design, methods, and supported use cases.  Most of the endpoints accept `JSON` as input and return `JSON` responses. This means that you must usually add the following headers to your request: ``` Content-type: application/json Accept: application/json ```  ## Resources  The term `resource` refers to a single type of object in the Airflow metadata. An API is broken up by its endpoint's corresponding resource. The name of a resource is typically plural and expressed in camelCase. Example: `dagRuns`.  Resource names are used as part of endpoint URLs, as well as in API parameters and responses.  ## CRUD Operations  The platform supports **C**reate, **R**ead, **U**pdate, and **D**elete operations on most resources. You can review the standards for these operations and their standard parameters below.  Some endpoints have special behavior as exceptions.  ### Create  To create a resource, you typically submit an HTTP `POST` request with the resource's required metadata in the request body. The response returns a `201 Created` response code upon success with the resource's metadata, including its internal `id`, in the response body.  ### Read  The HTTP `GET` request can be used to read a resource or to list a number of resources.  A resource's `id` can be submitted in the request parameters to read a specific resource. The response usually returns a `200 OK` response code upon success, with the resource's metadata in the response body.  If a `GET` request does not include a specific resource `id`, it is treated as a list request. The response usually returns a `200 OK` response code upon success, with an object containing a list of resources' metadata in the response body.  When reading resources, some common query parameters are usually available. e.g.: ``` v1/connections?limit=25&offset=25 ```  |Query Parameter|Type|Description| |---------------|----|-----------| |limit|integer|Maximum number of objects to fetch. Usually 25 by default| |offset|integer|Offset after which to start returning objects. For use with limit query parameter.|  ### Update  Updating a resource requires the resource `id`, and is typically done using an HTTP `PATCH` request, with the fields to modify in the request body. The response usually returns a `200 OK` response code upon success, with information about the modified resource in the response body.  ### Delete  Deleting a resource requires the resource `id` and is typically executing via an HTTP `DELETE` request. The response usually returns a `204 No Content` response code upon success.  ## Conventions  - Resource names are plural and expressed in camelCase. - Names are consistent between URL parameter name and field name.  - Field names are in snake_case. ```json {     \"name\": \"string\",     \"slots\": 0,     \"occupied_slots\": 0,     \"used_slots\": 0,     \"queued_slots\": 0,     \"open_slots\": 0 } ```  ### Update Mask  Update mask is available as a query parameter in patch endpoints. It is used to notify the API which fields you want to update. Using `update_mask` makes it easier to update objects by helping the server know which fields to update in an object instead of updating all fields. The update request ignores any fields that aren't specified in the field mask, leaving them with their current values.  Example: ```   resource = request.get('/resource/my-id').json()   resource['my_field'] = 'new-value'   request.patch('/resource/my-id?update_mask=my_field', data=json.dumps(resource)) ```  ## Versioning and Endpoint Lifecycle  - API versioning is not synchronized to specific releases of the Apache Airflow. - APIs are designed to be backward compatible. - Any changes to the API will first go through a deprecation phase.  # Summary of Changes  | Airflow version | Description | |-|-| | v2.0 | Initial release | | v2.0.2    | Added /plugins endpoint |  # Trying the API  You can use a third party client, such as [curl](https://curl.haxx.se/), [HTTPie](https://httpie.org/), [Postman](https://www.postman.com/) or [the Insomnia rest client](https://insomnia.rest/) to test the Apache Airflow API.  Note that you will need to pass credentials data.  For e.g., here is how to pause a DAG with [curl](https://curl.haxx.se/), when basic authorization is used: ```bash curl -X POST 'https://example.com/api/v1/dags/{dag_id}?update_mask=is_paused' \\ -H 'Content-Type: application/json' \\ --user \"username:password\" \\ -d '{     \"is_paused\": true }' ```  Using a graphical tool such as [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/), it is possible to import the API specifications directly:  1. Download the API specification by clicking the **Download** button at top of this document 2. Import the JSON specification in the graphical tool of your choice.   - In *Postman*, you can click the **import** button at the top   - With *Insomnia*, you can just drag-and-drop the file on the UI  Note that with *Postman*, you can also generate code snippets by selecting a request and clicking on the **Code** button.  ## Enabling CORS  [Cross-origin resource sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) is a browser security feature that restricts HTTP requests that are initiated from scripts running in the browser.  For details on enabling/configuring CORS, see [Enabling CORS](https://airflow.apache.org/docs/apache-airflow/stable/security/api.html).  # Authentication  To be able to meet the requirements of many organizations, Airflow supports many authentication methods, and it is even possible to add your own method.  If you want to check which auth backend is currently set, you can use `airflow config get-value api auth_backend` command as in the example below. ```bash $ airflow config get-value api auth_backend airflow.api.auth.backend.basic_auth ``` The default is to deny all requests.  For details on configuring the authentication, see [API Authorization](https://airflow.apache.org/docs/apache-airflow/stable/security/api.html).  # Errors  We follow the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs. As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Unauthenticated  This indicates that the request has not been applied because it lacks valid authentication credentials for the target resource. Please check that you have valid credentials.  ## PermissionDenied  This response means that the server understood the request but refuses to authorize it because it lacks sufficient rights to the resource. It happens when you do not have the necessary permission to execute the action you performed. You need to get the appropriate permissions in other to resolve this error.  ## BadRequest  This response means that the server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). To resolve this, please ensure that your syntax is correct.  ## NotFound  This client error response indicates that the server cannot find the requested resource.  ## MethodNotAllowed  Indicates that the request method is known by the server but is not supported by the target resource.  ## NotAcceptable  The target resource does not have a current representation that would be acceptable to the user agent, according to the proactive negotiation header fields received in the request, and the server is unwilling to supply a default representation.  ## AlreadyExists  The request could not be completed due to a conflict with the current state of the target resource, meaning that the resource already exists  ## Unknown  This means that the server encountered an unexpected condition that prevented it from fulfilling the request.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: dev@airflow.apache.org
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from airflow.configuration import Configuration


class ListDagRunsForm(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'page_offset': 'int',
        'page_limit': 'int',
        'dag_ids': 'list[str]',
        'execution_date_gte': 'datetime',
        'execution_date_lte': 'datetime',
        'start_date_gte': 'datetime',
        'start_date_lte': 'datetime',
        'end_date_gte': 'datetime',
        'end_date_lte': 'datetime'
    }

    attribute_map = {
        'page_offset': 'page_offset',
        'page_limit': 'page_limit',
        'dag_ids': 'dag_ids',
        'execution_date_gte': 'execution_date_gte',
        'execution_date_lte': 'execution_date_lte',
        'start_date_gte': 'start_date_gte',
        'start_date_lte': 'start_date_lte',
        'end_date_gte': 'end_date_gte',
        'end_date_lte': 'end_date_lte'
    }

    def __init__(self, page_offset=None, page_limit=100, dag_ids=None, execution_date_gte=None, execution_date_lte=None, start_date_gte=None, start_date_lte=None, end_date_gte=None, end_date_lte=None, local_vars_configuration=None):  # noqa: E501
        """ListDagRunsForm - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._page_offset = None
        self._page_limit = None
        self._dag_ids = None
        self._execution_date_gte = None
        self._execution_date_lte = None
        self._start_date_gte = None
        self._start_date_lte = None
        self._end_date_gte = None
        self._end_date_lte = None
        self.discriminator = None

        if page_offset is not None:
            self.page_offset = page_offset
        if page_limit is not None:
            self.page_limit = page_limit
        if dag_ids is not None:
            self.dag_ids = dag_ids
        if execution_date_gte is not None:
            self.execution_date_gte = execution_date_gte
        if execution_date_lte is not None:
            self.execution_date_lte = execution_date_lte
        if start_date_gte is not None:
            self.start_date_gte = start_date_gte
        if start_date_lte is not None:
            self.start_date_lte = start_date_lte
        if end_date_gte is not None:
            self.end_date_gte = end_date_gte
        if end_date_lte is not None:
            self.end_date_lte = end_date_lte

    @property
    def page_offset(self):
        """Gets the page_offset of this ListDagRunsForm.  # noqa: E501

        The number of items to skip before starting to collect the result set.  # noqa: E501

        :return: The page_offset of this ListDagRunsForm.  # noqa: E501
        :rtype: int
        """
        return self._page_offset

    @page_offset.setter
    def page_offset(self, page_offset):
        """Sets the page_offset of this ListDagRunsForm.

        The number of items to skip before starting to collect the result set.  # noqa: E501

        :param page_offset: The page_offset of this ListDagRunsForm.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                page_offset is not None and page_offset < 0):  # noqa: E501
            raise ValueError("Invalid value for `page_offset`, must be a value greater than or equal to `0`")  # noqa: E501

        self._page_offset = page_offset

    @property
    def page_limit(self):
        """Gets the page_limit of this ListDagRunsForm.  # noqa: E501

        The numbers of items to return.  # noqa: E501

        :return: The page_limit of this ListDagRunsForm.  # noqa: E501
        :rtype: int
        """
        return self._page_limit

    @page_limit.setter
    def page_limit(self, page_limit):
        """Sets the page_limit of this ListDagRunsForm.

        The numbers of items to return.  # noqa: E501

        :param page_limit: The page_limit of this ListDagRunsForm.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                page_limit is not None and page_limit < 1):  # noqa: E501
            raise ValueError("Invalid value for `page_limit`, must be a value greater than or equal to `1`")  # noqa: E501

        self._page_limit = page_limit

    @property
    def dag_ids(self):
        """Gets the dag_ids of this ListDagRunsForm.  # noqa: E501

        Return objects with specific DAG IDs. The value can be repeated to retrieve multiple matching values (OR condition).  # noqa: E501

        :return: The dag_ids of this ListDagRunsForm.  # noqa: E501
        :rtype: list[str]
        """
        return self._dag_ids

    @dag_ids.setter
    def dag_ids(self, dag_ids):
        """Sets the dag_ids of this ListDagRunsForm.

        Return objects with specific DAG IDs. The value can be repeated to retrieve multiple matching values (OR condition).  # noqa: E501

        :param dag_ids: The dag_ids of this ListDagRunsForm.  # noqa: E501
        :type: list[str]
        """

        self._dag_ids = dag_ids

    @property
    def execution_date_gte(self):
        """Gets the execution_date_gte of this ListDagRunsForm.  # noqa: E501

        Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte key to receive only the selected period.   # noqa: E501

        :return: The execution_date_gte of this ListDagRunsForm.  # noqa: E501
        :rtype: datetime
        """
        return self._execution_date_gte

    @execution_date_gte.setter
    def execution_date_gte(self, execution_date_gte):
        """Sets the execution_date_gte of this ListDagRunsForm.

        Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte key to receive only the selected period.   # noqa: E501

        :param execution_date_gte: The execution_date_gte of this ListDagRunsForm.  # noqa: E501
        :type: datetime
        """

        self._execution_date_gte = execution_date_gte

    @property
    def execution_date_lte(self):
        """Gets the execution_date_lte of this ListDagRunsForm.  # noqa: E501

        Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte key to receive only the selected period.   # noqa: E501

        :return: The execution_date_lte of this ListDagRunsForm.  # noqa: E501
        :rtype: datetime
        """
        return self._execution_date_lte

    @execution_date_lte.setter
    def execution_date_lte(self, execution_date_lte):
        """Sets the execution_date_lte of this ListDagRunsForm.

        Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte key to receive only the selected period.   # noqa: E501

        :param execution_date_lte: The execution_date_lte of this ListDagRunsForm.  # noqa: E501
        :type: datetime
        """

        self._execution_date_lte = execution_date_lte

    @property
    def start_date_gte(self):
        """Gets the start_date_gte of this ListDagRunsForm.  # noqa: E501

        Returns objects greater or equal the specified date.  This can be combined with start_date_lte key to receive only the selected period.   # noqa: E501

        :return: The start_date_gte of this ListDagRunsForm.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date_gte

    @start_date_gte.setter
    def start_date_gte(self, start_date_gte):
        """Sets the start_date_gte of this ListDagRunsForm.

        Returns objects greater or equal the specified date.  This can be combined with start_date_lte key to receive only the selected period.   # noqa: E501

        :param start_date_gte: The start_date_gte of this ListDagRunsForm.  # noqa: E501
        :type: datetime
        """

        self._start_date_gte = start_date_gte

    @property
    def start_date_lte(self):
        """Gets the start_date_lte of this ListDagRunsForm.  # noqa: E501

        Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period   # noqa: E501

        :return: The start_date_lte of this ListDagRunsForm.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date_lte

    @start_date_lte.setter
    def start_date_lte(self, start_date_lte):
        """Sets the start_date_lte of this ListDagRunsForm.

        Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period   # noqa: E501

        :param start_date_lte: The start_date_lte of this ListDagRunsForm.  # noqa: E501
        :type: datetime
        """

        self._start_date_lte = start_date_lte

    @property
    def end_date_gte(self):
        """Gets the end_date_gte of this ListDagRunsForm.  # noqa: E501

        Returns objects greater or equal the specified date.  This can be combined with end_date_lte parameter to receive only the selected period.   # noqa: E501

        :return: The end_date_gte of this ListDagRunsForm.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date_gte

    @end_date_gte.setter
    def end_date_gte(self, end_date_gte):
        """Sets the end_date_gte of this ListDagRunsForm.

        Returns objects greater or equal the specified date.  This can be combined with end_date_lte parameter to receive only the selected period.   # noqa: E501

        :param end_date_gte: The end_date_gte of this ListDagRunsForm.  # noqa: E501
        :type: datetime
        """

        self._end_date_gte = end_date_gte

    @property
    def end_date_lte(self):
        """Gets the end_date_lte of this ListDagRunsForm.  # noqa: E501

        Returns objects less than or equal to the specified date.  This can be combined with end_date_gte parameter to receive only the selected period.   # noqa: E501

        :return: The end_date_lte of this ListDagRunsForm.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date_lte

    @end_date_lte.setter
    def end_date_lte(self, end_date_lte):
        """Sets the end_date_lte of this ListDagRunsForm.

        Returns objects less than or equal to the specified date.  This can be combined with end_date_gte parameter to receive only the selected period.   # noqa: E501

        :param end_date_lte: The end_date_lte of this ListDagRunsForm.  # noqa: E501
        :type: datetime
        """

        self._end_date_lte = end_date_lte

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListDagRunsForm):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListDagRunsForm):
            return True

        return self.to_dict() != other.to_dict()
