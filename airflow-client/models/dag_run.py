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


class DAGRun(object):
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
        'dag_run_id': 'str',
        'dag_id': 'str',
        'execution_date': 'datetime',
        'start_date': 'datetime',
        'end_date': 'datetime',
        'state': 'DagState',
        'external_trigger': 'bool',
        'conf': 'object'
    }

    attribute_map = {
        'dag_run_id': 'dag_run_id',
        'dag_id': 'dag_id',
        'execution_date': 'execution_date',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'state': 'state',
        'external_trigger': 'external_trigger',
        'conf': 'conf'
    }

    def __init__(self, dag_run_id=None, dag_id=None, execution_date=None, start_date=None, end_date=None, state=None, external_trigger=True, conf=None, local_vars_configuration=None):  # noqa: E501
        """DAGRun - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dag_run_id = None
        self._dag_id = None
        self._execution_date = None
        self._start_date = None
        self._end_date = None
        self._state = None
        self._external_trigger = None
        self._conf = None
        self.discriminator = None

        self.dag_run_id = dag_run_id
        self.dag_id = dag_id
        if execution_date is not None:
            self.execution_date = execution_date
        if start_date is not None:
            self.start_date = start_date
        self.end_date = end_date
        if state is not None:
            self.state = state
        if external_trigger is not None:
            self.external_trigger = external_trigger
        if conf is not None:
            self.conf = conf

    @property
    def dag_run_id(self):
        """Gets the dag_run_id of this DAGRun.  # noqa: E501

        Run ID.  The value of this field can be set only when creating the object. If you try to modify the field of an existing object, the request fails with an BAD_REQUEST error.  If not provided, a value will be generated based on execution_date.  If the specified dag_run_id is in use, the creation request fails with an ALREADY_EXISTS error.  This together with DAG_ID are a unique key.   # noqa: E501

        :return: The dag_run_id of this DAGRun.  # noqa: E501
        :rtype: str
        """
        return self._dag_run_id

    @dag_run_id.setter
    def dag_run_id(self, dag_run_id):
        """Sets the dag_run_id of this DAGRun.

        Run ID.  The value of this field can be set only when creating the object. If you try to modify the field of an existing object, the request fails with an BAD_REQUEST error.  If not provided, a value will be generated based on execution_date.  If the specified dag_run_id is in use, the creation request fails with an ALREADY_EXISTS error.  This together with DAG_ID are a unique key.   # noqa: E501

        :param dag_run_id: The dag_run_id of this DAGRun.  # noqa: E501
        :type: str
        """

        self._dag_run_id = dag_run_id

    @property
    def dag_id(self):
        """Gets the dag_id of this DAGRun.  # noqa: E501


        :return: The dag_id of this DAGRun.  # noqa: E501
        :rtype: str
        """
        return self._dag_id

    @dag_id.setter
    def dag_id(self, dag_id):
        """Sets the dag_id of this DAGRun.


        :param dag_id: The dag_id of this DAGRun.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and dag_id is None:  # noqa: E501
            raise ValueError("Invalid value for `dag_id`, must not be `None`")  # noqa: E501

        self._dag_id = dag_id

    @property
    def execution_date(self):
        """Gets the execution_date of this DAGRun.  # noqa: E501

        The execution date. This is the time when the DAG run should be started according to the DAG definition. The value of this field can be set only when creating the object. If you try to modify the field of an existing object, the request fails with an BAD_REQUEST error. This together with DAG_ID are a unique key.   # noqa: E501

        :return: The execution_date of this DAGRun.  # noqa: E501
        :rtype: datetime
        """
        return self._execution_date

    @execution_date.setter
    def execution_date(self, execution_date):
        """Sets the execution_date of this DAGRun.

        The execution date. This is the time when the DAG run should be started according to the DAG definition. The value of this field can be set only when creating the object. If you try to modify the field of an existing object, the request fails with an BAD_REQUEST error. This together with DAG_ID are a unique key.   # noqa: E501

        :param execution_date: The execution_date of this DAGRun.  # noqa: E501
        :type: datetime
        """

        self._execution_date = execution_date

    @property
    def start_date(self):
        """Gets the start_date of this DAGRun.  # noqa: E501

        The start time. The time when DAG run was actually created.   # noqa: E501

        :return: The start_date of this DAGRun.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this DAGRun.

        The start time. The time when DAG run was actually created.   # noqa: E501

        :param start_date: The start_date of this DAGRun.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this DAGRun.  # noqa: E501


        :return: The end_date of this DAGRun.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this DAGRun.


        :param end_date: The end_date of this DAGRun.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def state(self):
        """Gets the state of this DAGRun.  # noqa: E501


        :return: The state of this DAGRun.  # noqa: E501
        :rtype: DagState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DAGRun.


        :param state: The state of this DAGRun.  # noqa: E501
        :type: DagState
        """

        self._state = state

    @property
    def external_trigger(self):
        """Gets the external_trigger of this DAGRun.  # noqa: E501


        :return: The external_trigger of this DAGRun.  # noqa: E501
        :rtype: bool
        """
        return self._external_trigger

    @external_trigger.setter
    def external_trigger(self, external_trigger):
        """Sets the external_trigger of this DAGRun.


        :param external_trigger: The external_trigger of this DAGRun.  # noqa: E501
        :type: bool
        """

        self._external_trigger = external_trigger

    @property
    def conf(self):
        """Gets the conf of this DAGRun.  # noqa: E501

        JSON object describing additional configuration parameters.  The value of this field can be set only when creating the object. If you try to modify the field of an existing object, the request fails with an BAD_REQUEST error.   # noqa: E501

        :return: The conf of this DAGRun.  # noqa: E501
        :rtype: object
        """
        return self._conf

    @conf.setter
    def conf(self, conf):
        """Sets the conf of this DAGRun.

        JSON object describing additional configuration parameters.  The value of this field can be set only when creating the object. If you try to modify the field of an existing object, the request fails with an BAD_REQUEST error.   # noqa: E501

        :param conf: The conf of this DAGRun.  # noqa: E501
        :type: object
        """

        self._conf = conf

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
        if not isinstance(other, DAGRun):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DAGRun):
            return True

        return self.to_dict() != other.to_dict()
