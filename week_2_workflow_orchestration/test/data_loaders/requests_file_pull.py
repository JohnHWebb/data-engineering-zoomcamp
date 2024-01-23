import io
import requests
from urllib.request import urlretrieve
from typing import Dict, List
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader


@data_loader
def load_data_from_api(urls: Dict, *args, **kwargs) -> List:
    url = urls['url']
    response = urlretrieve(url)

    return [response, urls['file_name']]