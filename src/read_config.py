import yaml
from pathlib import Path

def data(item_root:Path):
    global_doc = Path(__file__).parent / 'global_item.yaml'
    data = yaml.load(global_doc.read_text())

    local_doc = item_root / 'build' / 'item_config.yaml'
    if local_doc.exists():
        data.update(yaml.load(local_doc.read_text()))

    return data