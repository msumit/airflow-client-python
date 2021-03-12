# DAGDetail

DAG details.  For details see: (airflow.models.DAG)[https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/models/index.html#airflow.models.DAG] 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_id** | **str** | The ID of the DAG. | [optional] [readonly] 
**root_dag_id** | **str** | If the DAG is SubDAG then it is the top level DAG identifier. Otherwise, nulll. | [optional] [readonly] 
**is_paused** | **bool** | Whether the DAG is paused. | [optional] 
**is_subdag** | **bool** | Whether the DAG is SubDAG. | [optional] [readonly] 
**fileloc** | **str** | The absolute path to the file. | [optional] [readonly] 
**file_token** | **str** | The key containing the encrypted path to the file. Encryption and decryption take place only on the server. This prevents the client from reading an non-DAG file. This also ensures API extensibility, because the format of encrypted data may change.  | [optional] [readonly] 
**owners** | **list[str]** |  | [optional] [readonly] 
**description** | **str** | User-provided DAG description, which can consist of several sentences or paragraphs that describe DAG contents.  | [optional] [readonly] 
**schedule_interval** | [**ScheduleInterval**](ScheduleInterval.md) |  | [optional] 
**tags** | [**list[Tag]**](Tag.md) | List of tags. | [optional] [readonly] 
**timezone** | **str** |  | [optional] 
**catchup** | **bool** |  | [optional] [readonly] 
**orientation** | **str** |  | [optional] [readonly] 
**concurrency** | **float** |  | [optional] [readonly] 
**start_date** | **datetime** |  | [optional] [readonly] 
**dag_run_timeout** | [**TimeDelta**](TimeDelta.md) |  | [optional] 
**doc_md** | **str** |  | [optional] [readonly] 
**default_view** | **str** |  | [optional] [readonly] 
**params** | [**object**](.md) |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


