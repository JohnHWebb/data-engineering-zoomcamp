from os import path
from google.cloud import storage
import urllib3

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_google_cloud_storage(*args, **kwargs) -> None:

    # Generate urls
    url_base = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_"
    
    year = ''
    month = ''
    file_type = '.csv.gz'

    year = str(kwargs.get('interval_start_datetime').year)
    month = str(f'{kwargs.get("interval_start_datetime").month:02d}')

    url = url_base + year + '-' + month + file_type

    years = ['2019']
    months = ['04','05','06']

    for year in years:
        for month in months:
            url = f'{url_base}{year}-{month}{file_type}'
            file_name = f'yellow_tripdata_{year}-{month}{file_type}'
            
            bucket_name = 'yellow_taxi_data_raw'

            """Uploads a file to the bucket."""

            storage_client = storage.Client()
            bucket = storage_client.bucket(bucket_name)
            blob = bucket.blob(file_name)
            generation_match_precondition = 0

            
            blob.upload_from_filename(url, if_generation_match=generation_match_precondition)

            print(
                f"File {file_name} uploaded to {destination_blob_name}."
    )