if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer


@transformer
def transform(data: dict, *args, **kwargs) -> str:

    return (data[0].get('year') + '-' + data[0].get('month'))
