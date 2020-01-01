from .color import imp, sec
from .env import item_env
from .config import item_config
from .commander import item_commander

class item_core(item_env):
    def __init__(self):
        super().__init__()
        self.commander = item_commander(self)

    def run(self, command):
        return self.commander(command)