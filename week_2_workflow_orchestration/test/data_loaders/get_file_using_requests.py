if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
from typing import Dict, List
from mage_ai.io.file import FileIO



@data_loader
def load_data(url: Dict, *args, **kwargs) -> List:

    # Load CSV using FileIO, return file + filename
    df = FileIO.load(url['url'])
    file_name = url['file_name']
    return [df, file_name]