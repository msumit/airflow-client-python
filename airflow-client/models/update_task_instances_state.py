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

from airflow-client.configuration import Configuration


class UpdateTaskInstancesState(object):
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
        'dry_run': 'bool',
        'task_id': 'str',
        'execution_date': 'str',
        'include_upstream': 'bool',
        'include_downstream': 'bool',
        'include_future': 'bool',
        'include_past': 'bool',
        'new_state': 'str'
    }

    attribute_map = {
        'dry_run': 'dry_run',
        'task_id': 'task_id',
        'execution_date': 'execution_date',
        'include_upstream': 'include_upstream',
        'include_downstream': 'include_downstream',
        'include_future': 'include_future',
        'include_past': 'include_past',
        'new_state': 'new_state'
    }

    def __init__(self, dry_run=True, task_id=None, execution_date=None, include_upstream=None, include_downstream=None, include_future=None, include_past=None, new_state=None, local_vars_configuration=None):  # noqa: E501
        """UpdateTaskInstancesState - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dry_run = None
        self._task_id = None
        self._execution_date = None
        self._include_upstream = None
        self._include_downstream = None
        self._include_future = None
        self._include_past = None
        self._new_state = None
        self.discriminator = None

        if dry_run is not None:
            self.dry_run = dry_run
        if task_id is not None:
            self.task_id = task_id
        if execution_date is not None:
            self.execution_date = execution_date
        if include_upstream is not None:
            self.include_upstream = include_upstream
        if include_downstream is not None:
            self.include_downstream = include_downstream
        if include_future is not None:
            self.include_future = include_future
        if include_past is not None:
            self.include_past = include_past
        if new_state is not None:
            self.new_state = new_state

    @property
    def dry_run(self):
        """Gets the dry_run of this UpdateTaskInstancesState.  # noqa: E501

        If set, don't actually run this operation. The response will contain a list of task instances planned to be affected, but won't be modified in any way.   # noqa: E501

        :return: The dry_run of this UpdateTaskInstancesState.  # noqa: E501
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this UpdateTaskInstancesState.

        If set, don't actually run this operation. The response will contain a list of task instances planned to be affected, but won't be modified in any way.   # noqa: E501

        :param dry_run: The dry_run of this UpdateTaskInstancesState.  # noqa: E501
        :type: bool
        """

        self._dry_run = dry_run

    @property
    def task_id(self):
        """Gets the task_id of this UpdateTaskInstancesState.  # noqa: E501

        The task ID.  # noqa: E501

        :return: The task_id of this UpdateTaskInstancesState.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this UpdateTaskInstancesState.

        The task ID.  # noqa: E501

        :param task_id: The task_id of this UpdateTaskInstancesState.  # noqa: E501
        :type: str
        """

        self._task_id = task_id

    @property
    def execution_date(self):
        """Gets the execution_date of this UpdateTaskInstancesState.  # noqa: E501

        The execution date.  # noqa: E501

        :return: The execution_date of this UpdateTaskInstancesState.  # noqa: E501
        :rtype: str
        """
        return self._execution_date

    @execution_date.setter
    def execution_date(self, execution_date):
        """Sets the execution_date of this UpdateTaskInstancesState.

        The execution date.  # noqa: E501

        :param execution_date: The execution_date of this UpdateTaskInstancesState.  # noqa: E501
        :type: str
        """

        self._execution_date = execution_date

    @property
    def include_upstream(self):
        """Gets the include_upstream of this UpdateTaskInstancesState.  # noqa: E501

        If set to true, upstream tasks are also affected.  # noqa: E501

        :return: The include_upstream of this UpdateTaskInstancesState.  # noqa: E501
        :rtype: bool
        """
        return self._include_upstream

    @include_upstream.setter
    def include_upstream(self, include_upstream):
        """Sets the include_upstream of this UpdateTaskInstancesState.

        If set to true, upstream tasks are also affected.  # noqa: E501

        :param include_upstream: The include_upstream of this UpdateTaskInstancesState.  # noqa: E501
        :type: bool
        """

        self._include_upstream = include_upstream

    @property
    def include_downstream(self):
        """Gets the include_downstream of this UpdateTaskInstancesState.  # noqa: E501

        If set to true, downstream tasks are also affected.  # noqa: E501

        :return: The include_downstream of this UpdateTaskInstancesState.  # noqa: E501
        :rtype: bool
        """
        return self._include_downstream

    @include_downstream.setter
    def include_downstream(self, include_downstream):
        """Sets the include_downstream of this UpdateTaskInstancesState.

        If set to true, downstream tasks are also affected.  # noqa: E501

        :param include_downstream: The include_downstream of this UpdateTaskInstancesState.  # noqa: E501
        :type: bool
        """

        self._include_downstream = include_downstream

    @property
    def include_future(self):
        """Gets the include_future of this UpdateTaskInstancesState.  # noqa: E501

        If set to True, also tasks from future DAG Runs are affected.  # noqa: E501

        :return: The include_future of this UpdateTaskInstancesState.  # noqa: E501
        :rtype: bool
        """
        return self._include_future

    @include_future.setter
    def include_future(self, include_future):
        """Sets the include_future of this UpdateTaskInstancesState.

        If set to True, also tasks from future DAG Runs are affected.  # noqa: E501

        :param include_future: The include_future of this UpdateTaskInstancesState.  # noqa: E501
        :type: bool
        """

        self._include_future = include_future

    @property
    def include_past(self):
        """Gets the include_past of this UpdateTaskInstancesState.  # noqa: E501

        If set to True, also tasks from past DAG Runs are affected.  # noqa: E501

        :return: The include_past of this UpdateTaskInstancesState.  # noqa: E501
        :rtype: bool
        """
        return self._include_past

    @include_past.setter
    def include_past(self, include_past):
        """Sets the include_past of this UpdateTaskInstancesState.

        If set to True, also tasks from past DAG Runs are affected.  # noqa: E501

        :param include_past: The include_past of this UpdateTaskInstancesState.  # noqa: E501
        :type: bool
        """

        self._include_past = include_past

    @property
    def new_state(self):
        """Gets the new_state of this UpdateTaskInstancesState.  # noqa: E501

        Expected new state.  # noqa: E501

        :return: The new_state of this UpdateTaskInstancesState.  # noqa: E501
        :rtype: str
        """
        return self._new_state

    @new_state.setter
    def new_state(self, new_state):
        """Sets the new_state of this UpdateTaskInstancesState.

        Expected new state.  # noqa: E501

        :param new_state: The new_state of this UpdateTaskInstancesState.  # noqa: E501
        :type: str
        """
        allowed_values = ["success", "failed"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and new_state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `new_state` ({0}), must be one of {1}"  # noqa: E501
                .format(new_state, allowed_values)
            )

        self._new_state = new_state

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
        if not isinstance(other, UpdateTaskInstancesState):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateTaskInstancesState):
            return True

        return self.to_dict() != other.to_dict()
