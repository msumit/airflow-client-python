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


class ScheduleInterval(object):
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
        'type': 'str',
        'days': 'int',
        'seconds': 'int',
        'microseconds': 'int',
        'years': 'int',
        'months': 'int',
        'leapdays': 'int',
        'hours': 'int',
        'minutes': 'int',
        'year': 'int',
        'month': 'int',
        'day': 'int',
        'hour': 'int',
        'minute': 'int',
        'second': 'int',
        'microsecond': 'int',
        'value': 'str'
    }

    attribute_map = {
        'type': '__type',
        'days': 'days',
        'seconds': 'seconds',
        'microseconds': 'microseconds',
        'years': 'years',
        'months': 'months',
        'leapdays': 'leapdays',
        'hours': 'hours',
        'minutes': 'minutes',
        'year': 'year',
        'month': 'month',
        'day': 'day',
        'hour': 'hour',
        'minute': 'minute',
        'second': 'second',
        'microsecond': 'microsecond',
        'value': 'value'
    }

    discriminator_value_class_map = {
    }

    def __init__(self, type=None, days=None, seconds=None, microseconds=None, years=None, months=None, leapdays=None, hours=None, minutes=None, year=None, month=None, day=None, hour=None, minute=None, second=None, microsecond=None, value=None, local_vars_configuration=None):  # noqa: E501
        """ScheduleInterval - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._days = None
        self._seconds = None
        self._microseconds = None
        self._years = None
        self._months = None
        self._leapdays = None
        self._hours = None
        self._minutes = None
        self._year = None
        self._month = None
        self._day = None
        self._hour = None
        self._minute = None
        self._second = None
        self._microsecond = None
        self._value = None
        self.discriminator = 'type'

        self.type = type
        self.days = days
        self.seconds = seconds
        self.microseconds = microseconds
        self.years = years
        self.months = months
        self.leapdays = leapdays
        self.hours = hours
        self.minutes = minutes
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.microsecond = microsecond
        self.value = value

    @property
    def type(self):
        """Gets the type of this ScheduleInterval.  # noqa: E501


        :return: The type of this ScheduleInterval.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ScheduleInterval.


        :param type: The type of this ScheduleInterval.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def days(self):
        """Gets the days of this ScheduleInterval.  # noqa: E501


        :return: The days of this ScheduleInterval.  # noqa: E501
        :rtype: int
        """
        return self._days

    @days.setter
    def days(self, days):
        """Sets the days of this ScheduleInterval.


        :param days: The days of this ScheduleInterval.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and days is None:  # noqa: E501
            raise ValueError("Invalid value for `days`, must not be `None`")  # noqa: E501

        self._days = days

    @property
    def seconds(self):
        """Gets the seconds of this ScheduleInterval.  # noqa: E501


        :return: The seconds of this ScheduleInterval.  # noqa: E501
        :rtype: int
        """
        return self._seconds

    @seconds.setter
    def seconds(self, seconds):
        """Sets the seconds of this ScheduleInterval.


        :param seconds: The seconds of this ScheduleInterval.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and seconds is None:  # noqa: E501
            raise ValueError("Invalid value for `seconds`, must not be `None`")  # noqa: E501

        self._seconds = seconds

    @property
    def microseconds(self):
        """Gets the microseconds of this ScheduleInterval.  # noqa: E501


        :return: The microseconds of this ScheduleInterval.  # noqa: E501
        :rtype: int
        """
        return self._microseconds

    @microseconds.setter
    def microseconds(self, microseconds):
        """Sets the microseconds of this ScheduleInterval.


        :param microseconds: The microseconds of this ScheduleInterval.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and microseconds is None:  # noqa: E501
            raise ValueError("Invalid value for `microseconds`, must not be `None`")  # noqa: E501

        self._microseconds = microseconds

    @property
    def years(self):
        """Gets the years of this ScheduleInterval.  # noqa: E501


        :return: The years of this ScheduleInterval.  # noqa: E501
        :rtype: int
        """
        return self._years

    @years.setter
    def years(self, years):
        """Sets the years of this ScheduleInterval.


        :param years: The years of this ScheduleInterval.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and years is None:  # noqa: E501
            raise ValueError("Invalid value for `years`, must not be `None`")  # noqa: E501

        self._years = years

    @property
    def months(self):
        """Gets the months of this ScheduleInterval.  # noqa: E501


        :return: The months of this ScheduleInterval.  # noqa: E501
        :rtype: int
        """
        return self._months

    @months.setter
    def months(self, months):
        """Sets the months of this ScheduleInterval.


        :param months: The months of this ScheduleInterval.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and months is None:  # noqa: E501
            raise ValueError("Invalid value for `months`, must not be `None`")  # noqa: E501

        self._months = months

    @property
    def leapdays(self):
        """Gets the leapdays of this ScheduleInterval.  # noqa: E501


        :return: The leapdays of this ScheduleInterval.  # noqa: E501
        :rtype: int
        """
        return self._leapdays

    @leapdays.setter
    def leapdays(self, leapdays):
        """Sets the leapdays of this ScheduleInterval.


        :param leapdays: The leapdays of this ScheduleInterval.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and leapdays is None:  # noqa: E501
            raise ValueError("Invalid value for `leapdays`, must not be `None`")  # noqa: E501

        self._leapdays = leapdays

    @property
    def hours(self):
        """Gets the hours of this ScheduleInterval.  # noqa: E501


        :return: The hours of this ScheduleInterval.  # noqa: E501
        :rtype: int
        """
        return self._hours

    @hours.setter
    def hours(self, hours):
        """Sets the hours of this ScheduleInterval.


        :param hours: The hours of this ScheduleInterval.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and hours is None:  # noqa: E501
            raise ValueError("Invalid value for `hours`, must not be `None`")  # noqa: E501

        self._hours = hours

    @property
    def minutes(self):
        """Gets the minutes of this ScheduleInterval.  # noqa: E501


        :return: The minutes of this ScheduleInterval.  # noqa: E501
        :rtype: int
        """
        return self._minutes

    @minutes.setter
    def minutes(self, minutes):
        """Sets the minutes of this ScheduleInterval.


        :param minutes: The minutes of this ScheduleInterval.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and minutes is None:  # noqa: E501
            raise ValueError("Invalid value for `minutes`, must not be `None`")  # noqa: E501

        self._minutes = minutes

    @property
    def year(self):
        """Gets the year of this ScheduleInterval.  # noqa: E501


        :return: The year of this ScheduleInterval.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this ScheduleInterval.


        :param year: The year of this ScheduleInterval.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and year is None:  # noqa: E501
            raise ValueError("Invalid value for `year`, must not be `None`")  # noqa: E501

        self._year = year

    @property
    def month(self):
        """Gets the month of this ScheduleInterval.  # noqa: E501


        :return: The month of this ScheduleInterval.  # noqa: E501
        :rtype: int
        """
        return self._month

    @month.setter
    def month(self, month):
        """Sets the month of this ScheduleInterval.


        :param month: The month of this ScheduleInterval.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and month is None:  # noqa: E501
            raise ValueError("Invalid value for `month`, must not be `None`")  # noqa: E501

        self._month = month

    @property
    def day(self):
        """Gets the day of this ScheduleInterval.  # noqa: E501


        :return: The day of this ScheduleInterval.  # noqa: E501
        :rtype: int
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this ScheduleInterval.


        :param day: The day of this ScheduleInterval.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and day is None:  # noqa: E501
            raise ValueError("Invalid value for `day`, must not be `None`")  # noqa: E501

        self._day = day

    @property
    def hour(self):
        """Gets the hour of this ScheduleInterval.  # noqa: E501


        :return: The hour of this ScheduleInterval.  # noqa: E501
        :rtype: int
        """
        return self._hour

    @hour.setter
    def hour(self, hour):
        """Sets the hour of this ScheduleInterval.


        :param hour: The hour of this ScheduleInterval.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and hour is None:  # noqa: E501
            raise ValueError("Invalid value for `hour`, must not be `None`")  # noqa: E501

        self._hour = hour

    @property
    def minute(self):
        """Gets the minute of this ScheduleInterval.  # noqa: E501


        :return: The minute of this ScheduleInterval.  # noqa: E501
        :rtype: int
        """
        return self._minute

    @minute.setter
    def minute(self, minute):
        """Sets the minute of this ScheduleInterval.


        :param minute: The minute of this ScheduleInterval.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and minute is None:  # noqa: E501
            raise ValueError("Invalid value for `minute`, must not be `None`")  # noqa: E501

        self._minute = minute

    @property
    def second(self):
        """Gets the second of this ScheduleInterval.  # noqa: E501


        :return: The second of this ScheduleInterval.  # noqa: E501
        :rtype: int
        """
        return self._second

    @second.setter
    def second(self, second):
        """Sets the second of this ScheduleInterval.


        :param second: The second of this ScheduleInterval.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and second is None:  # noqa: E501
            raise ValueError("Invalid value for `second`, must not be `None`")  # noqa: E501

        self._second = second

    @property
    def microsecond(self):
        """Gets the microsecond of this ScheduleInterval.  # noqa: E501


        :return: The microsecond of this ScheduleInterval.  # noqa: E501
        :rtype: int
        """
        return self._microsecond

    @microsecond.setter
    def microsecond(self, microsecond):
        """Sets the microsecond of this ScheduleInterval.


        :param microsecond: The microsecond of this ScheduleInterval.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and microsecond is None:  # noqa: E501
            raise ValueError("Invalid value for `microsecond`, must not be `None`")  # noqa: E501

        self._microsecond = microsecond

    @property
    def value(self):
        """Gets the value of this ScheduleInterval.  # noqa: E501


        :return: The value of this ScheduleInterval.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ScheduleInterval.


        :param value: The value of this ScheduleInterval.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, ScheduleInterval):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScheduleInterval):
            return True

        return self.to_dict() != other.to_dict()
