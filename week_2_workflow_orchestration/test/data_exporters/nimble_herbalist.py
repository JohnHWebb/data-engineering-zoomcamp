from typing import Dict, List


@data_exporter
def export_data(users: List[Dict], **kwargs):
    print(users)