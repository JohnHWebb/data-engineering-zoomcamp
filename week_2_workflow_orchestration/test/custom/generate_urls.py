if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom


@custom
def transform_custom(*args, **kwargs):
    # Parameters
    url_base = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_"
    
    year = ''
    month = ''
    file_type = '.csv.gz'

    year = str(kwargs.get('interval_start_datetime').year)
    month = str(f'{kwargs.get("interval_start_datetime").month:02d}')

    url = url_base + year + '-' + month + file_type
    print(url)

    return 