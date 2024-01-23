if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
import requests

@custom
def transform_custom(*args, **kwargs):
    
    url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2019-01.csv.gz'
    response = requests.get(url)

    if type(response) != None:
        print("Success")
    else:
        print('Uh oh!')
    return