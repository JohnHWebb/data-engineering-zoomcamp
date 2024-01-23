if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
import requests
from google.cloud import storage
from io import BytesIO
import datetime

@custom
def transform_custom(*args, **kwargs):
    

    def download_file_to_memory(url):
        response = requests.get(url)
        if response.status_code == 200:
            return BytesIO(response.content)
        else:
            raise Exception(f"Failed to download file. Status code: {response.status_code}")

    def upload_to_google_cloud_storage(bucket_name, blob_name, data):
        client = storage.Client()
        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_file(data, content_type='application/octet-stream')

    year = str(kwargs.get('interval_start_datetime').year)
    month = str(f'{kwargs.get("interval_start_datetime").month:02d}')

    url_base = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_"
    file_type = '.csv.gz'
    url = f'{url_base}{year}-{month}{file_type}'

    google_storage_bucket = "green_taxi_data_raw"
    google_storage_blob_name = f'green_tripdata_{year}-{month}{file_type}'

    try:
        file_data = download_file_to_memory(url)
        upload_to_google_cloud_storage(google_storage_bucket, google_storage_blob_name, file_data)
        print(f"File {file_name} successfully uploaded to Google Cloud Storage.")
    except Exception as e:
        print(f"Error: {e}")

    return