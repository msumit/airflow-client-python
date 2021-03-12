# airflow-client.XComApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_xcom_entries**](XComApi.md#get_xcom_entries) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/xcomEntries | List XCom entries
[**get_xcom_entry**](XComApi.md#get_xcom_entry) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/xcomEntries/{xcom_key} | Get an XCom entry


# **get_xcom_entries**
> XComCollection get_xcom_entries(dag_id, dag_run_id, task_id, limit=limit, offset=offset)

List XCom entries

This endpoint allows specifying `~` as the dag_id, dag_run_id, task_id to retrieve XCOM entries for for all DAGs, DAG runs and task instances. XCom values won't be returned as they can be large. Use this endpoint to get a list of XCom entries and then fetch individual entry to get value.

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
    api_instance = airflow-client.XComApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
dag_run_id = 'dag_run_id_example' # str | The DAG run ID.
task_id = 'task_id_example' # str | The task ID.
limit = 100 # int | The numbers of items to return. (optional) (default to 100)
offset = 56 # int | The number of items to skip before starting to collect the result set. (optional)

    try:
        # List XCom entries
        api_response = api_instance.get_xcom_entries(dag_id, dag_run_id, task_id, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling XComApi->get_xcom_entries: %s\n" % e)
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
    api_instance = airflow-client.XComApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
dag_run_id = 'dag_run_id_example' # str | The DAG run ID.
task_id = 'task_id_example' # str | The task ID.
limit = 100 # int | The numbers of items to return. (optional) (default to 100)
offset = 56 # int | The number of items to skip before starting to collect the result set. (optional)

    try:
        # List XCom entries
        api_response = api_instance.get_xcom_entries(dag_id, dag_run_id, task_id, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling XComApi->get_xcom_entries: %s\n" % e)
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
    api_instance = airflow-client.XComApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
dag_run_id = 'dag_run_id_example' # str | The DAG run ID.
task_id = 'task_id_example' # str | The task ID.
limit = 100 # int | The numbers of items to return. (optional) (default to 100)
offset = 56 # int | The number of items to skip before starting to collect the result set. (optional)

    try:
        # List XCom entries
        api_response = api_instance.get_xcom_entries(dag_id, dag_run_id, task_id, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling XComApi->get_xcom_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. | 
 **dag_run_id** | **str**| The DAG run ID. | 
 **task_id** | **str**| The task ID. | 
 **limit** | **int**| The numbers of items to return. | [optional] [default to 100]
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional] 

### Return type

[**XComCollection**](XComCollection.md)

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

# **get_xcom_entry**
> XCom get_xcom_entry(dag_id, dag_run_id, task_id, xcom_key)

Get an XCom entry

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
    api_instance = airflow-client.XComApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
dag_run_id = 'dag_run_id_example' # str | The DAG run ID.
task_id = 'task_id_example' # str | The task ID.
xcom_key = 'xcom_key_example' # str | The XCom key.

    try:
        # Get an XCom entry
        api_response = api_instance.get_xcom_entry(dag_id, dag_run_id, task_id, xcom_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling XComApi->get_xcom_entry: %s\n" % e)
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
    api_instance = airflow-client.XComApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
dag_run_id = 'dag_run_id_example' # str | The DAG run ID.
task_id = 'task_id_example' # str | The task ID.
xcom_key = 'xcom_key_example' # str | The XCom key.

    try:
        # Get an XCom entry
        api_response = api_instance.get_xcom_entry(dag_id, dag_run_id, task_id, xcom_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling XComApi->get_xcom_entry: %s\n" % e)
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
    api_instance = airflow-client.XComApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
dag_run_id = 'dag_run_id_example' # str | The DAG run ID.
task_id = 'task_id_example' # str | The task ID.
xcom_key = 'xcom_key_example' # str | The XCom key.

    try:
        # Get an XCom entry
        api_response = api_instance.get_xcom_entry(dag_id, dag_run_id, task_id, xcom_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling XComApi->get_xcom_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. | 
 **dag_run_id** | **str**| The DAG run ID. | 
 **task_id** | **str**| The task ID. | 
 **xcom_key** | **str**| The XCom key. | 

### Return type

[**XCom**](XCom.md)

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

