if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter
from typing import Dict, List


@data_exporter
def export_data(data: List, *args, **kwargs):
    print(data)