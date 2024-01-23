if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
from datetime import datetime
import pandas as pd


@data_loader
def load_data(*args, **kwargs) -> list:
    

    # Parameters
    url_base = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_"
    
    # Check if kwargs contains date data, otherwise default to something
    year = ''
    month = ''
    file_type = '.csv.gz'

    year = str(kwargs.get('interval_start_datetime').year)
    month = str(f'{kwargs.get("interval_start_datetime").month:02d}')

    url = url_base + year + '-' + month + file_type
    print(url)
    
    df = pd.read_csv(url_base + year + '-' + month + file_type)
    file_name = f'yellow_tripdata_{year}-{month}{file_type}'
    

    return [df, file_name]