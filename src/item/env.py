from .path import item_path
from .config import item_config
from .color import imp, sec

class item_env(object):
    def __init__(self, path=None):
        self.path = item_path(path)
        self.local_config = item_config(self.path / 'build' / 'item_config.yaml')
        self.global_config = item_config(item_path(__file__).parent / 'global_item_config.yaml')

    # ----------------------------------------------------------

    def is_item_root(self):
        # if there is 'item_config.yaml' in dir './build',
        # then it is a 'item'
        return self.local_config.yaml_file_exists()

    # -----------------------------------------------------------

    def _reload_local_config(self):
        self.local_config = item_config(self.path / 'build' / 'item_config.yaml')