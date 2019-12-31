from pathlib import Path
from .config import item_config
from .color import imp, sec

class item_env(object):
    def __init__(self, path:Path=None):
        if path != None:
            self.path = path
        else:
            self.path = Path.cwd()
        self.local_config = item_config(self.path / 'build' / 'item_config.yaml')
        self.global_config = item_config(Path(__file__).parent / 'global_item_config.yaml')

    # ----------------------------------------------------------

    def ls(self):
        for file_ in list(self.path.iterdir()):
            print(sec(file_.name))

    def cd(self, other_path:str or Path):
        '''will charge the self.path'''
        self.path /= other_path
        self._reload_local_config()

    def helper(self):
        # item: /path/to/item(under item) >_
        # else: /path/to/non-item >_
        if self.is_item_root():
            return imp(f'{self.path}') + sec('(under item) ') + imp('> ')
        else:
            return imp(f'{self.path} > ')

    def get_vaild_file(self, path):
        _path = self.path / path
        while True:
            print(sec('please enter the file name following:'))
            self.ls()
            input_ = input(sec('(enter ?q to leave)> '))
            if input_ == '?q':
                break
            elif (_path / input_).exists():
                return (_path / input_)

    def is_item_root(self):
        # if there is 'item_config.yaml' in dir './build',
        # then it is a 'item'
        return self.local_config.yaml_file_exists()

    # -----------------------------------------------------------

    def _reload_local_config(self):
        self.local_config = item_config(self.item_root.path / 'build' / 'item_config.yaml')