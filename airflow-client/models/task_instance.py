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


class TaskInstance(object):
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
        'task_id': 'str',
        'dag_id': 'str',
        'execution_date': 'str',
        'start_date': 'str',
        'end_date': 'str',
        'duration': 'float',
        'state': 'TaskState',
        'try_number': 'int',
        'max_tries': 'int',
        'hostname': 'str',
        'unixname': 'str',
        'pool': 'str',
        'pool_slots': 'int',
        'queue': 'str',
        'priority_weight': 'int',
        'operator': 'str',
        'queued_when': 'str',
        'pid': 'int',
        'executor_config': 'str',
        'sla_miss': 'SLAMiss'
    }

    attribute_map = {
        'task_id': 'task_id',
        'dag_id': 'dag_id',
        'execution_date': 'execution_date',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'duration': 'duration',
        'state': 'state',
        'try_number': 'try_number',
        'max_tries': 'max_tries',
        'hostname': 'hostname',
        'unixname': 'unixname',
        'pool': 'pool',
        'pool_slots': 'pool_slots',
        'queue': 'queue',
        'priority_weight': 'priority_weight',
        'operator': 'operator',
        'queued_when': 'queued_when',
        'pid': 'pid',
        'executor_config': 'executor_config',
        'sla_miss': 'sla_miss'
    }

    def __init__(self, task_id=None, dag_id=None, execution_date=None, start_date=None, end_date=None, duration=None, state=None, try_number=None, max_tries=None, hostname=None, unixname=None, pool=None, pool_slots=None, queue=None, priority_weight=None, operator=None, queued_when=None, pid=None, executor_config=None, sla_miss=None, local_vars_configuration=None):  # noqa: E501
        """TaskInstance - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._task_id = None
        self._dag_id = None
        self._execution_date = None
        self._start_date = None
        self._end_date = None
        self._duration = None
        self._state = None
        self._try_number = None
        self._max_tries = None
        self._hostname = None
        self._unixname = None
        self._pool = None
        self._pool_slots = None
        self._queue = None
        self._priority_weight = None
        self._operator = None
        self._queued_when = None
        self._pid = None
        self._executor_config = None
        self._sla_miss = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if dag_id is not None:
            self.dag_id = dag_id
        if execution_date is not None:
            self.execution_date = execution_date
        self.start_date = start_date
        self.end_date = end_date
        self.duration = duration
        if state is not None:
            self.state = state
        if try_number is not None:
            self.try_number = try_number
        if max_tries is not None:
            self.max_tries = max_tries
        if hostname is not None:
            self.hostname = hostname
        if unixname is not None:
            self.unixname = unixname
        if pool is not None:
            self.pool = pool
        if pool_slots is not None:
            self.pool_slots = pool_slots
        if queue is not None:
            self.queue = queue
        if priority_weight is not None:
            self.priority_weight = priority_weight
        if operator is not None:
            self.operator = operator
        self.queued_when = queued_when
        self.pid = pid
        if executor_config is not None:
            self.executor_config = executor_config
        if sla_miss is not None:
            self.sla_miss = sla_miss

    @property
    def task_id(self):
        """Gets the task_id of this TaskInstance.  # noqa: E501


        :return: The task_id of this TaskInstance.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this TaskInstance.


        :param task_id: The task_id of this TaskInstance.  # noqa: E501
        :type: str
        """

        self._task_id = task_id

    @property
    def dag_id(self):
        """Gets the dag_id of this TaskInstance.  # noqa: E501


        :return: The dag_id of this TaskInstance.  # noqa: E501
        :rtype: str
        """
        return self._dag_id

    @dag_id.setter
    def dag_id(self, dag_id):
        """Sets the dag_id of this TaskInstance.


        :param dag_id: The dag_id of this TaskInstance.  # noqa: E501
        :type: str
        """

        self._dag_id = dag_id

    @property
    def execution_date(self):
        """Gets the execution_date of this TaskInstance.  # noqa: E501


        :return: The execution_date of this TaskInstance.  # noqa: E501
        :rtype: str
        """
        return self._execution_date

    @execution_date.setter
    def execution_date(self, execution_date):
        """Sets the execution_date of this TaskInstance.


        :param execution_date: The execution_date of this TaskInstance.  # noqa: E501
        :type: str
        """

        self._execution_date = execution_date

    @property
    def start_date(self):
        """Gets the start_date of this TaskInstance.  # noqa: E501


        :return: The start_date of this TaskInstance.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this TaskInstance.


        :param start_date: The start_date of this TaskInstance.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this TaskInstance.  # noqa: E501


        :return: The end_date of this TaskInstance.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this TaskInstance.


        :param end_date: The end_date of this TaskInstance.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def duration(self):
        """Gets the duration of this TaskInstance.  # noqa: E501


        :return: The duration of this TaskInstance.  # noqa: E501
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this TaskInstance.


        :param duration: The duration of this TaskInstance.  # noqa: E501
        :type: float
        """

        self._duration = duration

    @property
    def state(self):
        """Gets the state of this TaskInstance.  # noqa: E501


        :return: The state of this TaskInstance.  # noqa: E501
        :rtype: TaskState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this TaskInstance.


        :param state: The state of this TaskInstance.  # noqa: E501
        :type: TaskState
        """

        self._state = state

    @property
    def try_number(self):
        """Gets the try_number of this TaskInstance.  # noqa: E501


        :return: The try_number of this TaskInstance.  # noqa: E501
        :rtype: int
        """
        return self._try_number

    @try_number.setter
    def try_number(self, try_number):
        """Sets the try_number of this TaskInstance.


        :param try_number: The try_number of this TaskInstance.  # noqa: E501
        :type: int
        """

        self._try_number = try_number

    @property
    def max_tries(self):
        """Gets the max_tries of this TaskInstance.  # noqa: E501


        :return: The max_tries of this TaskInstance.  # noqa: E501
        :rtype: int
        """
        return self._max_tries

    @max_tries.setter
    def max_tries(self, max_tries):
        """Sets the max_tries of this TaskInstance.


        :param max_tries: The max_tries of this TaskInstance.  # noqa: E501
        :type: int
        """

        self._max_tries = max_tries

    @property
    def hostname(self):
        """Gets the hostname of this TaskInstance.  # noqa: E501


        :return: The hostname of this TaskInstance.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this TaskInstance.


        :param hostname: The hostname of this TaskInstance.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def unixname(self):
        """Gets the unixname of this TaskInstance.  # noqa: E501


        :return: The unixname of this TaskInstance.  # noqa: E501
        :rtype: str
        """
        return self._unixname

    @unixname.setter
    def unixname(self, unixname):
        """Sets the unixname of this TaskInstance.


        :param unixname: The unixname of this TaskInstance.  # noqa: E501
        :type: str
        """

        self._unixname = unixname

    @property
    def pool(self):
        """Gets the pool of this TaskInstance.  # noqa: E501


        :return: The pool of this TaskInstance.  # noqa: E501
        :rtype: str
        """
        return self._pool

    @pool.setter
    def pool(self, pool):
        """Sets the pool of this TaskInstance.


        :param pool: The pool of this TaskInstance.  # noqa: E501
        :type: str
        """

        self._pool = pool

    @property
    def pool_slots(self):
        """Gets the pool_slots of this TaskInstance.  # noqa: E501


        :return: The pool_slots of this TaskInstance.  # noqa: E501
        :rtype: int
        """
        return self._pool_slots

    @pool_slots.setter
    def pool_slots(self, pool_slots):
        """Sets the pool_slots of this TaskInstance.


        :param pool_slots: The pool_slots of this TaskInstance.  # noqa: E501
        :type: int
        """

        self._pool_slots = pool_slots

    @property
    def queue(self):
        """Gets the queue of this TaskInstance.  # noqa: E501


        :return: The queue of this TaskInstance.  # noqa: E501
        :rtype: str
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        """Sets the queue of this TaskInstance.


        :param queue: The queue of this TaskInstance.  # noqa: E501
        :type: str
        """

        self._queue = queue

    @property
    def priority_weight(self):
        """Gets the priority_weight of this TaskInstance.  # noqa: E501


        :return: The priority_weight of this TaskInstance.  # noqa: E501
        :rtype: int
        """
        return self._priority_weight

    @priority_weight.setter
    def priority_weight(self, priority_weight):
        """Sets the priority_weight of this TaskInstance.


        :param priority_weight: The priority_weight of this TaskInstance.  # noqa: E501
        :type: int
        """

        self._priority_weight = priority_weight

    @property
    def operator(self):
        """Gets the operator of this TaskInstance.  # noqa: E501


        :return: The operator of this TaskInstance.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this TaskInstance.


        :param operator: The operator of this TaskInstance.  # noqa: E501
        :type: str
        """

        self._operator = operator

    @property
    def queued_when(self):
        """Gets the queued_when of this TaskInstance.  # noqa: E501


        :return: The queued_when of this TaskInstance.  # noqa: E501
        :rtype: str
        """
        return self._queued_when

    @queued_when.setter
    def queued_when(self, queued_when):
        """Sets the queued_when of this TaskInstance.


        :param queued_when: The queued_when of this TaskInstance.  # noqa: E501
        :type: str
        """

        self._queued_when = queued_when

    @property
    def pid(self):
        """Gets the pid of this TaskInstance.  # noqa: E501


        :return: The pid of this TaskInstance.  # noqa: E501
        :rtype: int
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """Sets the pid of this TaskInstance.


        :param pid: The pid of this TaskInstance.  # noqa: E501
        :type: int
        """

        self._pid = pid

    @property
    def executor_config(self):
        """Gets the executor_config of this TaskInstance.  # noqa: E501


        :return: The executor_config of this TaskInstance.  # noqa: E501
        :rtype: str
        """
        return self._executor_config

    @executor_config.setter
    def executor_config(self, executor_config):
        """Sets the executor_config of this TaskInstance.


        :param executor_config: The executor_config of this TaskInstance.  # noqa: E501
        :type: str
        """

        self._executor_config = executor_config

    @property
    def sla_miss(self):
        """Gets the sla_miss of this TaskInstance.  # noqa: E501


        :return: The sla_miss of this TaskInstance.  # noqa: E501
        :rtype: SLAMiss
        """
        return self._sla_miss

    @sla_miss.setter
    def sla_miss(self, sla_miss):
        """Sets the sla_miss of this TaskInstance.


        :param sla_miss: The sla_miss of this TaskInstance.  # noqa: E501
        :type: SLAMiss
        """

        self._sla_miss = sla_miss

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
        if not isinstance(other, TaskInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskInstance):
            return True

        return self.to_dict() != other.to_dict()
