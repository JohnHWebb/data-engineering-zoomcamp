if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
from typing import Dict, List
import requests

@custom
def transform_custom(urls: Dict, *args, **kwargs) -> Dict:
    """
    args: The output from any upstream parent blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    url = urls['url']
    response = requests.get(url)

    return dict(file=response, file_name=urls['file_name'])