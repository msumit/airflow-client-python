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


class Task(object):
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
        'class_ref': 'ClassReference',
        'task_id': 'str',
        'owner': 'str',
        'start_date': 'datetime',
        'end_date': 'datetime',
        'trigger_rule': 'TriggerRule',
        'extra_links': 'list[TaskExtraLinks]',
        'depends_on_past': 'bool',
        'wait_for_downstream': 'bool',
        'retries': 'float',
        'queue': 'str',
        'pool': 'str',
        'pool_slots': 'float',
        'execution_timeout': 'TimeDelta',
        'retry_delay': 'TimeDelta',
        'retry_exponential_backoff': 'bool',
        'priority_weight': 'float',
        'weight_rule': 'WeightRule',
        'ui_color': 'str',
        'ui_fgcolor': 'str',
        'template_fields': 'list[str]',
        'sub_dag': 'DAG',
        'downstream_task_ids': 'list[str]'
    }

    attribute_map = {
        'class_ref': 'class_ref',
        'task_id': 'task_id',
        'owner': 'owner',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'trigger_rule': 'trigger_rule',
        'extra_links': 'extra_links',
        'depends_on_past': 'depends_on_past',
        'wait_for_downstream': 'wait_for_downstream',
        'retries': 'retries',
        'queue': 'queue',
        'pool': 'pool',
        'pool_slots': 'pool_slots',
        'execution_timeout': 'execution_timeout',
        'retry_delay': 'retry_delay',
        'retry_exponential_backoff': 'retry_exponential_backoff',
        'priority_weight': 'priority_weight',
        'weight_rule': 'weight_rule',
        'ui_color': 'ui_color',
        'ui_fgcolor': 'ui_fgcolor',
        'template_fields': 'template_fields',
        'sub_dag': 'sub_dag',
        'downstream_task_ids': 'downstream_task_ids'
    }

    def __init__(self, class_ref=None, task_id=None, owner=None, start_date=None, end_date=None, trigger_rule=None, extra_links=None, depends_on_past=None, wait_for_downstream=None, retries=None, queue=None, pool=None, pool_slots=None, execution_timeout=None, retry_delay=None, retry_exponential_backoff=None, priority_weight=None, weight_rule=None, ui_color=None, ui_fgcolor=None, template_fields=None, sub_dag=None, downstream_task_ids=None, local_vars_configuration=None):  # noqa: E501
        """Task - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._class_ref = None
        self._task_id = None
        self._owner = None
        self._start_date = None
        self._end_date = None
        self._trigger_rule = None
        self._extra_links = None
        self._depends_on_past = None
        self._wait_for_downstream = None
        self._retries = None
        self._queue = None
        self._pool = None
        self._pool_slots = None
        self._execution_timeout = None
        self._retry_delay = None
        self._retry_exponential_backoff = None
        self._priority_weight = None
        self._weight_rule = None
        self._ui_color = None
        self._ui_fgcolor = None
        self._template_fields = None
        self._sub_dag = None
        self._downstream_task_ids = None
        self.discriminator = None

        if class_ref is not None:
            self.class_ref = class_ref
        if task_id is not None:
            self.task_id = task_id
        if owner is not None:
            self.owner = owner
        if start_date is not None:
            self.start_date = start_date
        self.end_date = end_date
        if trigger_rule is not None:
            self.trigger_rule = trigger_rule
        if extra_links is not None:
            self.extra_links = extra_links
        if depends_on_past is not None:
            self.depends_on_past = depends_on_past
        if wait_for_downstream is not None:
            self.wait_for_downstream = wait_for_downstream
        if retries is not None:
            self.retries = retries
        if queue is not None:
            self.queue = queue
        if pool is not None:
            self.pool = pool
        if pool_slots is not None:
            self.pool_slots = pool_slots
        if execution_timeout is not None:
            self.execution_timeout = execution_timeout
        if retry_delay is not None:
            self.retry_delay = retry_delay
        if retry_exponential_backoff is not None:
            self.retry_exponential_backoff = retry_exponential_backoff
        if priority_weight is not None:
            self.priority_weight = priority_weight
        if weight_rule is not None:
            self.weight_rule = weight_rule
        if ui_color is not None:
            self.ui_color = ui_color
        if ui_fgcolor is not None:
            self.ui_fgcolor = ui_fgcolor
        if template_fields is not None:
            self.template_fields = template_fields
        if sub_dag is not None:
            self.sub_dag = sub_dag
        if downstream_task_ids is not None:
            self.downstream_task_ids = downstream_task_ids

    @property
    def class_ref(self):
        """Gets the class_ref of this Task.  # noqa: E501


        :return: The class_ref of this Task.  # noqa: E501
        :rtype: ClassReference
        """
        return self._class_ref

    @class_ref.setter
    def class_ref(self, class_ref):
        """Sets the class_ref of this Task.


        :param class_ref: The class_ref of this Task.  # noqa: E501
        :type: ClassReference
        """

        self._class_ref = class_ref

    @property
    def task_id(self):
        """Gets the task_id of this Task.  # noqa: E501


        :return: The task_id of this Task.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this Task.


        :param task_id: The task_id of this Task.  # noqa: E501
        :type: str
        """

        self._task_id = task_id

    @property
    def owner(self):
        """Gets the owner of this Task.  # noqa: E501


        :return: The owner of this Task.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Task.


        :param owner: The owner of this Task.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def start_date(self):
        """Gets the start_date of this Task.  # noqa: E501


        :return: The start_date of this Task.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Task.


        :param start_date: The start_date of this Task.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this Task.  # noqa: E501


        :return: The end_date of this Task.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this Task.


        :param end_date: The end_date of this Task.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def trigger_rule(self):
        """Gets the trigger_rule of this Task.  # noqa: E501


        :return: The trigger_rule of this Task.  # noqa: E501
        :rtype: TriggerRule
        """
        return self._trigger_rule

    @trigger_rule.setter
    def trigger_rule(self, trigger_rule):
        """Sets the trigger_rule of this Task.


        :param trigger_rule: The trigger_rule of this Task.  # noqa: E501
        :type: TriggerRule
        """

        self._trigger_rule = trigger_rule

    @property
    def extra_links(self):
        """Gets the extra_links of this Task.  # noqa: E501


        :return: The extra_links of this Task.  # noqa: E501
        :rtype: list[TaskExtraLinks]
        """
        return self._extra_links

    @extra_links.setter
    def extra_links(self, extra_links):
        """Sets the extra_links of this Task.


        :param extra_links: The extra_links of this Task.  # noqa: E501
        :type: list[TaskExtraLinks]
        """

        self._extra_links = extra_links

    @property
    def depends_on_past(self):
        """Gets the depends_on_past of this Task.  # noqa: E501


        :return: The depends_on_past of this Task.  # noqa: E501
        :rtype: bool
        """
        return self._depends_on_past

    @depends_on_past.setter
    def depends_on_past(self, depends_on_past):
        """Sets the depends_on_past of this Task.


        :param depends_on_past: The depends_on_past of this Task.  # noqa: E501
        :type: bool
        """

        self._depends_on_past = depends_on_past

    @property
    def wait_for_downstream(self):
        """Gets the wait_for_downstream of this Task.  # noqa: E501


        :return: The wait_for_downstream of this Task.  # noqa: E501
        :rtype: bool
        """
        return self._wait_for_downstream

    @wait_for_downstream.setter
    def wait_for_downstream(self, wait_for_downstream):
        """Sets the wait_for_downstream of this Task.


        :param wait_for_downstream: The wait_for_downstream of this Task.  # noqa: E501
        :type: bool
        """

        self._wait_for_downstream = wait_for_downstream

    @property
    def retries(self):
        """Gets the retries of this Task.  # noqa: E501


        :return: The retries of this Task.  # noqa: E501
        :rtype: float
        """
        return self._retries

    @retries.setter
    def retries(self, retries):
        """Sets the retries of this Task.


        :param retries: The retries of this Task.  # noqa: E501
        :type: float
        """

        self._retries = retries

    @property
    def queue(self):
        """Gets the queue of this Task.  # noqa: E501


        :return: The queue of this Task.  # noqa: E501
        :rtype: str
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        """Sets the queue of this Task.


        :param queue: The queue of this Task.  # noqa: E501
        :type: str
        """

        self._queue = queue

    @property
    def pool(self):
        """Gets the pool of this Task.  # noqa: E501


        :return: The pool of this Task.  # noqa: E501
        :rtype: str
        """
        return self._pool

    @pool.setter
    def pool(self, pool):
        """Sets the pool of this Task.


        :param pool: The pool of this Task.  # noqa: E501
        :type: str
        """

        self._pool = pool

    @property
    def pool_slots(self):
        """Gets the pool_slots of this Task.  # noqa: E501


        :return: The pool_slots of this Task.  # noqa: E501
        :rtype: float
        """
        return self._pool_slots

    @pool_slots.setter
    def pool_slots(self, pool_slots):
        """Sets the pool_slots of this Task.


        :param pool_slots: The pool_slots of this Task.  # noqa: E501
        :type: float
        """

        self._pool_slots = pool_slots

    @property
    def execution_timeout(self):
        """Gets the execution_timeout of this Task.  # noqa: E501


        :return: The execution_timeout of this Task.  # noqa: E501
        :rtype: TimeDelta
        """
        return self._execution_timeout

    @execution_timeout.setter
    def execution_timeout(self, execution_timeout):
        """Sets the execution_timeout of this Task.


        :param execution_timeout: The execution_timeout of this Task.  # noqa: E501
        :type: TimeDelta
        """

        self._execution_timeout = execution_timeout

    @property
    def retry_delay(self):
        """Gets the retry_delay of this Task.  # noqa: E501


        :return: The retry_delay of this Task.  # noqa: E501
        :rtype: TimeDelta
        """
        return self._retry_delay

    @retry_delay.setter
    def retry_delay(self, retry_delay):
        """Sets the retry_delay of this Task.


        :param retry_delay: The retry_delay of this Task.  # noqa: E501
        :type: TimeDelta
        """

        self._retry_delay = retry_delay

    @property
    def retry_exponential_backoff(self):
        """Gets the retry_exponential_backoff of this Task.  # noqa: E501


        :return: The retry_exponential_backoff of this Task.  # noqa: E501
        :rtype: bool
        """
        return self._retry_exponential_backoff

    @retry_exponential_backoff.setter
    def retry_exponential_backoff(self, retry_exponential_backoff):
        """Sets the retry_exponential_backoff of this Task.


        :param retry_exponential_backoff: The retry_exponential_backoff of this Task.  # noqa: E501
        :type: bool
        """

        self._retry_exponential_backoff = retry_exponential_backoff

    @property
    def priority_weight(self):
        """Gets the priority_weight of this Task.  # noqa: E501


        :return: The priority_weight of this Task.  # noqa: E501
        :rtype: float
        """
        return self._priority_weight

    @priority_weight.setter
    def priority_weight(self, priority_weight):
        """Sets the priority_weight of this Task.


        :param priority_weight: The priority_weight of this Task.  # noqa: E501
        :type: float
        """

        self._priority_weight = priority_weight

    @property
    def weight_rule(self):
        """Gets the weight_rule of this Task.  # noqa: E501


        :return: The weight_rule of this Task.  # noqa: E501
        :rtype: WeightRule
        """
        return self._weight_rule

    @weight_rule.setter
    def weight_rule(self, weight_rule):
        """Sets the weight_rule of this Task.


        :param weight_rule: The weight_rule of this Task.  # noqa: E501
        :type: WeightRule
        """

        self._weight_rule = weight_rule

    @property
    def ui_color(self):
        """Gets the ui_color of this Task.  # noqa: E501

        Color in hexadecimal notation.  # noqa: E501

        :return: The ui_color of this Task.  # noqa: E501
        :rtype: str
        """
        return self._ui_color

    @ui_color.setter
    def ui_color(self, ui_color):
        """Sets the ui_color of this Task.

        Color in hexadecimal notation.  # noqa: E501

        :param ui_color: The ui_color of this Task.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                ui_color is not None and not re.search(r'^#[a-fA-F0-9]{3,6}$', ui_color)):  # noqa: E501
            raise ValueError(r"Invalid value for `ui_color`, must be a follow pattern or equal to `/^#[a-fA-F0-9]{3,6}$/`")  # noqa: E501

        self._ui_color = ui_color

    @property
    def ui_fgcolor(self):
        """Gets the ui_fgcolor of this Task.  # noqa: E501

        Color in hexadecimal notation.  # noqa: E501

        :return: The ui_fgcolor of this Task.  # noqa: E501
        :rtype: str
        """
        return self._ui_fgcolor

    @ui_fgcolor.setter
    def ui_fgcolor(self, ui_fgcolor):
        """Sets the ui_fgcolor of this Task.

        Color in hexadecimal notation.  # noqa: E501

        :param ui_fgcolor: The ui_fgcolor of this Task.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                ui_fgcolor is not None and not re.search(r'^#[a-fA-F0-9]{3,6}$', ui_fgcolor)):  # noqa: E501
            raise ValueError(r"Invalid value for `ui_fgcolor`, must be a follow pattern or equal to `/^#[a-fA-F0-9]{3,6}$/`")  # noqa: E501

        self._ui_fgcolor = ui_fgcolor

    @property
    def template_fields(self):
        """Gets the template_fields of this Task.  # noqa: E501


        :return: The template_fields of this Task.  # noqa: E501
        :rtype: list[str]
        """
        return self._template_fields

    @template_fields.setter
    def template_fields(self, template_fields):
        """Sets the template_fields of this Task.


        :param template_fields: The template_fields of this Task.  # noqa: E501
        :type: list[str]
        """

        self._template_fields = template_fields

    @property
    def sub_dag(self):
        """Gets the sub_dag of this Task.  # noqa: E501


        :return: The sub_dag of this Task.  # noqa: E501
        :rtype: DAG
        """
        return self._sub_dag

    @sub_dag.setter
    def sub_dag(self, sub_dag):
        """Sets the sub_dag of this Task.


        :param sub_dag: The sub_dag of this Task.  # noqa: E501
        :type: DAG
        """

        self._sub_dag = sub_dag

    @property
    def downstream_task_ids(self):
        """Gets the downstream_task_ids of this Task.  # noqa: E501


        :return: The downstream_task_ids of this Task.  # noqa: E501
        :rtype: list[str]
        """
        return self._downstream_task_ids

    @downstream_task_ids.setter
    def downstream_task_ids(self, downstream_task_ids):
        """Sets the downstream_task_ids of this Task.


        :param downstream_task_ids: The downstream_task_ids of this Task.  # noqa: E501
        :type: list[str]
        """

        self._downstream_task_ids = downstream_task_ids

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
        if not isinstance(other, Task):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Task):
            return True

        return self.to_dict() != other.to_dict()
