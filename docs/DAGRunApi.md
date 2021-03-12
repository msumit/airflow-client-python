# airflow-client.DAGRunApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_dag_run**](DAGRunApi.md#delete_dag_run) | **DELETE** /dags/{dag_id}/dagRuns/{dag_run_id} | Delete a DAG run
[**get_dag_run**](DAGRunApi.md#get_dag_run) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id} | Get a DAG run
[**get_dag_runs**](DAGRunApi.md#get_dag_runs) | **GET** /dags/{dag_id}/dagRuns | List DAG runs
[**get_dag_runs_batch**](DAGRunApi.md#get_dag_runs_batch) | **POST** /dags/~/dagRuns/list | List DAG runs (batch)
[**post_dag_run**](DAGRunApi.md#post_dag_run) | **POST** /dags/{dag_id}/dagRuns | Trigger a new DAG run


# **delete_dag_run**
> delete_dag_run(dag_id, dag_run_id)

Delete a DAG run

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
    api_instance = airflow-client.DAGRunApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
dag_run_id = 'dag_run_id_example' # str | The DAG run ID.

    try:
        # Delete a DAG run
        api_instance.delete_dag_run(dag_id, dag_run_id)
    except ApiException as e:
        print("Exception when calling DAGRunApi->delete_dag_run: %s\n" % e)
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
    api_instance = airflow-client.DAGRunApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
dag_run_id = 'dag_run_id_example' # str | The DAG run ID.

    try:
        # Delete a DAG run
        api_instance.delete_dag_run(dag_id, dag_run_id)
    except ApiException as e:
        print("Exception when calling DAGRunApi->delete_dag_run: %s\n" % e)
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
    api_instance = airflow-client.DAGRunApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
dag_run_id = 'dag_run_id_example' # str | The DAG run ID.

    try:
        # Delete a DAG run
        api_instance.delete_dag_run(dag_id, dag_run_id)
    except ApiException as e:
        print("Exception when calling DAGRunApi->delete_dag_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. | 
 **dag_run_id** | **str**| The DAG run ID. | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [GoogleOpenId](../README.md#GoogleOpenId), [Kerberos](../README.md#Kerberos)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success. |  -  |
**400** | Client specified an invalid argument. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |
**404** | A specified resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dag_run**
> DAGRun get_dag_run(dag_id, dag_run_id)

Get a DAG run

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
    api_instance = airflow-client.DAGRunApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
dag_run_id = 'dag_run_id_example' # str | The DAG run ID.

    try:
        # Get a DAG run
        api_response = api_instance.get_dag_run(dag_id, dag_run_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DAGRunApi->get_dag_run: %s\n" % e)
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
    api_instance = airflow-client.DAGRunApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
dag_run_id = 'dag_run_id_example' # str | The DAG run ID.

    try:
        # Get a DAG run
        api_response = api_instance.get_dag_run(dag_id, dag_run_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DAGRunApi->get_dag_run: %s\n" % e)
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
    api_instance = airflow-client.DAGRunApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
dag_run_id = 'dag_run_id_example' # str | The DAG run ID.

    try:
        # Get a DAG run
        api_response = api_instance.get_dag_run(dag_id, dag_run_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DAGRunApi->get_dag_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. | 
 **dag_run_id** | **str**| The DAG run ID. | 

### Return type

[**DAGRun**](DAGRun.md)

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

# **get_dag_runs**
> DAGRunCollection get_dag_runs(dag_id, limit=limit, offset=offset, execution_date_gte=execution_date_gte, execution_date_lte=execution_date_lte, start_date_gte=start_date_gte, start_date_lte=start_date_lte, end_date_gte=end_date_gte, end_date_lte=end_date_lte)

List DAG runs

This endpoint allows specifying `~` as the dag_id to retrieve DAG runs for all DAGs. 

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
    api_instance = airflow-client.DAGRunApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
limit = 100 # int | The numbers of items to return. (optional) (default to 100)
offset = 56 # int | The number of items to skip before starting to collect the result set. (optional)
execution_date_gte = '2013-10-20T19:20:30+01:00' # datetime | Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte parameter to receive only the selected period.  (optional)
execution_date_lte = '2013-10-20T19:20:30+01:00' # datetime | Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte parameter to receive only the selected period.  (optional)
start_date_gte = '2013-10-20T19:20:30+01:00' # datetime | Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  (optional)
start_date_lte = '2013-10-20T19:20:30+01:00' # datetime | Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  (optional)
end_date_gte = '2013-10-20T19:20:30+01:00' # datetime | Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  (optional)
end_date_lte = '2013-10-20T19:20:30+01:00' # datetime | Returns objects less than or equal to the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  (optional)

    try:
        # List DAG runs
        api_response = api_instance.get_dag_runs(dag_id, limit=limit, offset=offset, execution_date_gte=execution_date_gte, execution_date_lte=execution_date_lte, start_date_gte=start_date_gte, start_date_lte=start_date_lte, end_date_gte=end_date_gte, end_date_lte=end_date_lte)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DAGRunApi->get_dag_runs: %s\n" % e)
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
    api_instance = airflow-client.DAGRunApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
limit = 100 # int | The numbers of items to return. (optional) (default to 100)
offset = 56 # int | The number of items to skip before starting to collect the result set. (optional)
execution_date_gte = '2013-10-20T19:20:30+01:00' # datetime | Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte parameter to receive only the selected period.  (optional)
execution_date_lte = '2013-10-20T19:20:30+01:00' # datetime | Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte parameter to receive only the selected period.  (optional)
start_date_gte = '2013-10-20T19:20:30+01:00' # datetime | Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  (optional)
start_date_lte = '2013-10-20T19:20:30+01:00' # datetime | Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  (optional)
end_date_gte = '2013-10-20T19:20:30+01:00' # datetime | Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  (optional)
end_date_lte = '2013-10-20T19:20:30+01:00' # datetime | Returns objects less than or equal to the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  (optional)

    try:
        # List DAG runs
        api_response = api_instance.get_dag_runs(dag_id, limit=limit, offset=offset, execution_date_gte=execution_date_gte, execution_date_lte=execution_date_lte, start_date_gte=start_date_gte, start_date_lte=start_date_lte, end_date_gte=end_date_gte, end_date_lte=end_date_lte)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DAGRunApi->get_dag_runs: %s\n" % e)
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
    api_instance = airflow-client.DAGRunApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
limit = 100 # int | The numbers of items to return. (optional) (default to 100)
offset = 56 # int | The number of items to skip before starting to collect the result set. (optional)
execution_date_gte = '2013-10-20T19:20:30+01:00' # datetime | Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte parameter to receive only the selected period.  (optional)
execution_date_lte = '2013-10-20T19:20:30+01:00' # datetime | Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte parameter to receive only the selected period.  (optional)
start_date_gte = '2013-10-20T19:20:30+01:00' # datetime | Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  (optional)
start_date_lte = '2013-10-20T19:20:30+01:00' # datetime | Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  (optional)
end_date_gte = '2013-10-20T19:20:30+01:00' # datetime | Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  (optional)
end_date_lte = '2013-10-20T19:20:30+01:00' # datetime | Returns objects less than or equal to the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  (optional)

    try:
        # List DAG runs
        api_response = api_instance.get_dag_runs(dag_id, limit=limit, offset=offset, execution_date_gte=execution_date_gte, execution_date_lte=execution_date_lte, start_date_gte=start_date_gte, start_date_lte=start_date_lte, end_date_gte=end_date_gte, end_date_lte=end_date_lte)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DAGRunApi->get_dag_runs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. | 
 **limit** | **int**| The numbers of items to return. | [optional] [default to 100]
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional] 
 **execution_date_gte** | **datetime**| Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte parameter to receive only the selected period.  | [optional] 
 **execution_date_lte** | **datetime**| Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte parameter to receive only the selected period.  | [optional] 
 **start_date_gte** | **datetime**| Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  | [optional] 
 **start_date_lte** | **datetime**| Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  | [optional] 
 **end_date_gte** | **datetime**| Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  | [optional] 
 **end_date_lte** | **datetime**| Returns objects less than or equal to the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  | [optional] 

### Return type

[**DAGRunCollection**](DAGRunCollection.md)

### Authorization

[Basic](../README.md#Basic), [GoogleOpenId](../README.md#GoogleOpenId), [Kerberos](../README.md#Kerberos)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of DAG runs. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dag_runs_batch**
> DAGRunCollection get_dag_runs_batch(list_dag_runs_form)

List DAG runs (batch)

This endpoint is a POST to allow filtering across a large number of DAG IDs, where as a GET it would run in to maximum HTTP request URL length limit. 

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
    api_instance = airflow-client.DAGRunApi(api_client)
    list_dag_runs_form = airflow-client.ListDagRunsForm() # ListDagRunsForm | 

    try:
        # List DAG runs (batch)
        api_response = api_instance.get_dag_runs_batch(list_dag_runs_form)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DAGRunApi->get_dag_runs_batch: %s\n" % e)
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
    api_instance = airflow-client.DAGRunApi(api_client)
    list_dag_runs_form = airflow-client.ListDagRunsForm() # ListDagRunsForm | 

    try:
        # List DAG runs (batch)
        api_response = api_instance.get_dag_runs_batch(list_dag_runs_form)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DAGRunApi->get_dag_runs_batch: %s\n" % e)
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
    api_instance = airflow-client.DAGRunApi(api_client)
    list_dag_runs_form = airflow-client.ListDagRunsForm() # ListDagRunsForm | 

    try:
        # List DAG runs (batch)
        api_response = api_instance.get_dag_runs_batch(list_dag_runs_form)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DAGRunApi->get_dag_runs_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_dag_runs_form** | [**ListDagRunsForm**](ListDagRunsForm.md)|  | 

### Return type

[**DAGRunCollection**](DAGRunCollection.md)

### Authorization

[Basic](../README.md#Basic), [GoogleOpenId](../README.md#GoogleOpenId), [Kerberos](../README.md#Kerberos)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Client specified an invalid argument. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_dag_run**
> DAGRun post_dag_run(dag_id, dag_run)

Trigger a new DAG run

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
    api_instance = airflow-client.DAGRunApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
dag_run = airflow-client.DAGRun() # DAGRun | 

    try:
        # Trigger a new DAG run
        api_response = api_instance.post_dag_run(dag_id, dag_run)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DAGRunApi->post_dag_run: %s\n" % e)
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
    api_instance = airflow-client.DAGRunApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
dag_run = airflow-client.DAGRun() # DAGRun | 

    try:
        # Trigger a new DAG run
        api_response = api_instance.post_dag_run(dag_id, dag_run)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DAGRunApi->post_dag_run: %s\n" % e)
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
    api_instance = airflow-client.DAGRunApi(api_client)
    dag_id = 'dag_id_example' # str | The DAG ID.
dag_run = airflow-client.DAGRun() # DAGRun | 

    try:
        # Trigger a new DAG run
        api_response = api_instance.post_dag_run(dag_id, dag_run)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DAGRunApi->post_dag_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. | 
 **dag_run** | [**DAGRun**](DAGRun.md)|  | 

### Return type

[**DAGRun**](DAGRun.md)

### Authorization

[Basic](../README.md#Basic), [GoogleOpenId](../README.md#GoogleOpenId), [Kerberos](../README.md#Kerberos)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Client specified an invalid argument. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**409** | The resource that a client tried to create already exists. |  -  |
**403** | Client does not have sufficient permission. |  -  |
**404** | A specified resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

