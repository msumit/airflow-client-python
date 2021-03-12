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


class PluginCollectionItem(object):
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
        'number': 'str',
        'name': 'str',
        'hooks': 'list[str]',
        'executors': 'list[str]',
        'macros': 'list[object]',
        'flask_blueprints': 'list[object]',
        'appbuilder_views': 'list[object]',
        'appbuilder_menu_items': 'list[object]',
        'global_operator_extra_links': 'list[object]',
        'operator_extra_links': 'list[object]',
        'source': 'str'
    }

    attribute_map = {
        'number': 'number',
        'name': 'name',
        'hooks': 'hooks',
        'executors': 'executors',
        'macros': 'macros',
        'flask_blueprints': 'flask_blueprints',
        'appbuilder_views': 'appbuilder_views',
        'appbuilder_menu_items': 'appbuilder_menu_items',
        'global_operator_extra_links': 'global_operator_extra_links',
        'operator_extra_links': 'operator_extra_links',
        'source': 'source'
    }

    def __init__(self, number=None, name=None, hooks=None, executors=None, macros=None, flask_blueprints=None, appbuilder_views=None, appbuilder_menu_items=None, global_operator_extra_links=None, operator_extra_links=None, source=None, local_vars_configuration=None):  # noqa: E501
        """PluginCollectionItem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._number = None
        self._name = None
        self._hooks = None
        self._executors = None
        self._macros = None
        self._flask_blueprints = None
        self._appbuilder_views = None
        self._appbuilder_menu_items = None
        self._global_operator_extra_links = None
        self._operator_extra_links = None
        self._source = None
        self.discriminator = None

        if number is not None:
            self.number = number
        if name is not None:
            self.name = name
        if hooks is not None:
            self.hooks = hooks
        if executors is not None:
            self.executors = executors
        if macros is not None:
            self.macros = macros
        if flask_blueprints is not None:
            self.flask_blueprints = flask_blueprints
        if appbuilder_views is not None:
            self.appbuilder_views = appbuilder_views
        if appbuilder_menu_items is not None:
            self.appbuilder_menu_items = appbuilder_menu_items
        if global_operator_extra_links is not None:
            self.global_operator_extra_links = global_operator_extra_links
        if operator_extra_links is not None:
            self.operator_extra_links = operator_extra_links
        self.source = source

    @property
    def number(self):
        """Gets the number of this PluginCollectionItem.  # noqa: E501

        The plugin number  # noqa: E501

        :return: The number of this PluginCollectionItem.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this PluginCollectionItem.

        The plugin number  # noqa: E501

        :param number: The number of this PluginCollectionItem.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def name(self):
        """Gets the name of this PluginCollectionItem.  # noqa: E501

        The name of the plugin  # noqa: E501

        :return: The name of this PluginCollectionItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PluginCollectionItem.

        The name of the plugin  # noqa: E501

        :param name: The name of this PluginCollectionItem.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def hooks(self):
        """Gets the hooks of this PluginCollectionItem.  # noqa: E501

        The plugin hooks  # noqa: E501

        :return: The hooks of this PluginCollectionItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._hooks

    @hooks.setter
    def hooks(self, hooks):
        """Sets the hooks of this PluginCollectionItem.

        The plugin hooks  # noqa: E501

        :param hooks: The hooks of this PluginCollectionItem.  # noqa: E501
        :type: list[str]
        """

        self._hooks = hooks

    @property
    def executors(self):
        """Gets the executors of this PluginCollectionItem.  # noqa: E501

        The plugin executors  # noqa: E501

        :return: The executors of this PluginCollectionItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._executors

    @executors.setter
    def executors(self, executors):
        """Sets the executors of this PluginCollectionItem.

        The plugin executors  # noqa: E501

        :param executors: The executors of this PluginCollectionItem.  # noqa: E501
        :type: list[str]
        """

        self._executors = executors

    @property
    def macros(self):
        """Gets the macros of this PluginCollectionItem.  # noqa: E501

        The plugin macros  # noqa: E501

        :return: The macros of this PluginCollectionItem.  # noqa: E501
        :rtype: list[object]
        """
        return self._macros

    @macros.setter
    def macros(self, macros):
        """Sets the macros of this PluginCollectionItem.

        The plugin macros  # noqa: E501

        :param macros: The macros of this PluginCollectionItem.  # noqa: E501
        :type: list[object]
        """

        self._macros = macros

    @property
    def flask_blueprints(self):
        """Gets the flask_blueprints of this PluginCollectionItem.  # noqa: E501

        The flask blueprints  # noqa: E501

        :return: The flask_blueprints of this PluginCollectionItem.  # noqa: E501
        :rtype: list[object]
        """
        return self._flask_blueprints

    @flask_blueprints.setter
    def flask_blueprints(self, flask_blueprints):
        """Sets the flask_blueprints of this PluginCollectionItem.

        The flask blueprints  # noqa: E501

        :param flask_blueprints: The flask_blueprints of this PluginCollectionItem.  # noqa: E501
        :type: list[object]
        """

        self._flask_blueprints = flask_blueprints

    @property
    def appbuilder_views(self):
        """Gets the appbuilder_views of this PluginCollectionItem.  # noqa: E501

        The appuilder views  # noqa: E501

        :return: The appbuilder_views of this PluginCollectionItem.  # noqa: E501
        :rtype: list[object]
        """
        return self._appbuilder_views

    @appbuilder_views.setter
    def appbuilder_views(self, appbuilder_views):
        """Sets the appbuilder_views of this PluginCollectionItem.

        The appuilder views  # noqa: E501

        :param appbuilder_views: The appbuilder_views of this PluginCollectionItem.  # noqa: E501
        :type: list[object]
        """

        self._appbuilder_views = appbuilder_views

    @property
    def appbuilder_menu_items(self):
        """Gets the appbuilder_menu_items of this PluginCollectionItem.  # noqa: E501

        The Flask Appbuilder menu items  # noqa: E501

        :return: The appbuilder_menu_items of this PluginCollectionItem.  # noqa: E501
        :rtype: list[object]
        """
        return self._appbuilder_menu_items

    @appbuilder_menu_items.setter
    def appbuilder_menu_items(self, appbuilder_menu_items):
        """Sets the appbuilder_menu_items of this PluginCollectionItem.

        The Flask Appbuilder menu items  # noqa: E501

        :param appbuilder_menu_items: The appbuilder_menu_items of this PluginCollectionItem.  # noqa: E501
        :type: list[object]
        """

        self._appbuilder_menu_items = appbuilder_menu_items

    @property
    def global_operator_extra_links(self):
        """Gets the global_operator_extra_links of this PluginCollectionItem.  # noqa: E501

        The global operator extra links  # noqa: E501

        :return: The global_operator_extra_links of this PluginCollectionItem.  # noqa: E501
        :rtype: list[object]
        """
        return self._global_operator_extra_links

    @global_operator_extra_links.setter
    def global_operator_extra_links(self, global_operator_extra_links):
        """Sets the global_operator_extra_links of this PluginCollectionItem.

        The global operator extra links  # noqa: E501

        :param global_operator_extra_links: The global_operator_extra_links of this PluginCollectionItem.  # noqa: E501
        :type: list[object]
        """

        self._global_operator_extra_links = global_operator_extra_links

    @property
    def operator_extra_links(self):
        """Gets the operator_extra_links of this PluginCollectionItem.  # noqa: E501

        Operator extra links  # noqa: E501

        :return: The operator_extra_links of this PluginCollectionItem.  # noqa: E501
        :rtype: list[object]
        """
        return self._operator_extra_links

    @operator_extra_links.setter
    def operator_extra_links(self, operator_extra_links):
        """Sets the operator_extra_links of this PluginCollectionItem.

        Operator extra links  # noqa: E501

        :param operator_extra_links: The operator_extra_links of this PluginCollectionItem.  # noqa: E501
        :type: list[object]
        """

        self._operator_extra_links = operator_extra_links

    @property
    def source(self):
        """Gets the source of this PluginCollectionItem.  # noqa: E501

        The plugin source  # noqa: E501

        :return: The source of this PluginCollectionItem.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this PluginCollectionItem.

        The plugin source  # noqa: E501

        :param source: The source of this PluginCollectionItem.  # noqa: E501
        :type: str
        """

        self._source = source

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
        if not isinstance(other, PluginCollectionItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PluginCollectionItem):
            return True

        return self.to_dict() != other.to_dict()
