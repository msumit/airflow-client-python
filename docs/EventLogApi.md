# airflow-client.EventLogApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event_log**](EventLogApi.md#get_event_log) | **GET** /eventLogs/{event_log_id} | Get a log entry
[**get_event_logs**](EventLogApi.md#get_event_logs) | **GET** /eventLogs | List log entries


# **get_event_log**
> EventLog get_event_log(event_log_id)

Get a log entry

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import airflow-client
from airflow-client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = airflow-client.Configuration(
    host = "http://localhost/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = airflow-client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with airflow-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airflow-client.EventLogApi(api_client)
    event_log_id = 56 # int | The event log ID.

    try:
        # Get a log entry
        api_response = api_instance.get_event_log(event_log_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventLogApi->get_event_log: %s\n" % e)
```

```python
from __future__ import print_function
import time
import airflow-client
from airflow-client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = airflow-client.Configuration(
    host = "http://localhost/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = airflow-client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with airflow-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airflow-client.EventLogApi(api_client)
    event_log_id = 56 # int | The event log ID.

    try:
        # Get a log entry
        api_response = api_instance.get_event_log(event_log_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventLogApi->get_event_log: %s\n" % e)
```

```python
from __future__ import print_function
import time
import airflow-client
from airflow-client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = airflow-client.Configuration(
    host = "http://localhost/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = airflow-client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with airflow-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airflow-client.EventLogApi(api_client)
    event_log_id = 56 # int | The event log ID.

    try:
        # Get a log entry
        api_response = api_instance.get_event_log(event_log_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventLogApi->get_event_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_log_id** | **int**| The event log ID. | 

### Return type

[**EventLog**](EventLog.md)

### Authorization

[Basic](../README.md#Basic), [GoogleOpenId](../README.md#GoogleOpenId), [Kerberos](../README.md#Kerberos)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |
**404** | A specified resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_logs**
> EventLogCollection get_event_logs(limit=limit, offset=offset)

List log entries

List log entries from event log.

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import airflow-client
from airflow-client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = airflow-client.Configuration(
    host = "http://localhost/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = airflow-client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with airflow-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airflow-client.EventLogApi(api_client)
    limit = 100 # int | The numbers of items to return. (optional) (default to 100)
offset = 56 # int | The number of items to skip before starting to collect the result set. (optional)

    try:
        # List log entries
        api_response = api_instance.get_event_logs(limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventLogApi->get_event_logs: %s\n" % e)
```

```python
from __future__ import print_function
import time
import airflow-client
from airflow-client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = airflow-client.Configuration(
    host = "http://localhost/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = airflow-client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with airflow-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airflow-client.EventLogApi(api_client)
    limit = 100 # int | The numbers of items to return. (optional) (default to 100)
offset = 56 # int | The number of items to skip before starting to collect the result set. (optional)

    try:
        # List log entries
        api_response = api_instance.get_event_logs(limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventLogApi->get_event_logs: %s\n" % e)
```

```python
from __future__ import print_function
import time
import airflow-client
from airflow-client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = airflow-client.Configuration(
    host = "http://localhost/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = airflow-client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with airflow-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = airflow-client.EventLogApi(api_client)
    limit = 100 # int | The numbers of items to return. (optional) (default to 100)
offset = 56 # int | The number of items to skip before starting to collect the result set. (optional)

    try:
        # List log entries
        api_response = api_instance.get_event_logs(limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventLogApi->get_event_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The numbers of items to return. | [optional] [default to 100]
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional] 

### Return type

[**EventLogCollection**](EventLogCollection.md)

### Authorization

[Basic](../README.md#Basic), [GoogleOpenId](../README.md#GoogleOpenId), [Kerberos](../README.md#Kerberos)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

