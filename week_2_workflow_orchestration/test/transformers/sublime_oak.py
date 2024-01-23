from typing import Dict, List
import uuid


@transformer
def transform(data: Dict, *args, **kwargs) -> List[Dict]:
    data['token'] = uuid.uuid4().hex
    return [data]from typing import Dict, List


@data_exporter
def export_data(users: List[Dict], **kwargs):
    print(users)