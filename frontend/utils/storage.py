from azure.storage.blob import BlobServiceClient, ContentSettings
from azure.data.tables import TableServiceClient
from azure.identity import EnvironmentCredential
from datetime import datetime

timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
credential = EnvironmentCredential()

def upload_file_to_blob(blob_conn_str, container_name, file):
    blob_service = BlobServiceClient.from_connection_string(blob_conn_str)
    blob_name = f"{timestamp}_" + file.filename
    blob_client = blob_service.get_blob_client(container=container_name, blob=blob_name)
    blob_client.upload_blob(file, overwrite=True, content_settings=ContentSettings(content_type=file.content_type))
    return blob_name

def store_metadata_in_table(table_conn_str, table_name, blob_name, from_user, to_user):
    table_service = TableServiceClient.from_connection_string(table_conn_str)
    table_client = table_service.get_table_client(table_name=table_name)
    entity = {
        "PartitionKey": "filemeta",
        "RowKey": blob_name,
        "from_user": from_user,
        "to_user": to_user
    }
    table_client.upsert_entity(entity)
