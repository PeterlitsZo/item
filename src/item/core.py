from pathlib import Path
from .color import imp, sec
from .get_Path import get_parent_dir_ls
from .config import config, _data

class item():
    def __init__(self):
        self.item_root = Path.cwd()
        try:
            self.config = _data(self.item_root / 'build' / 'item_config.yaml')
        except:
            self.config = {}
        self.global_config = _data(Path(__file__).parent / 'global_item_config.yaml')

    def init(self, *command):
        # make a current dir be an 'item'
        # self.is_item(): False -> True
        if len(command) > 1:
            command = command[0]
            print(f"command is too long, taste as 'init {command}''")
        elif len(command) == 0:
            print(f"init need the case like 'init cpp'")
        else:
            command = command[0]

        if not self.is_item():
            local_config = self.item_root / 'build' / 'item_config.yaml'
            global_config = Path(__file__).parent / 'global_item_config.yaml'
            config(global_config, local_config, command, self.item_root)

        else:
            print(imp('you are already are in inited item, I can\'t init it twice'))

    def is_item(self):
        # if there is 'item_config.yaml' in dir './build',
        # then it is a 'item'
        return (self.item_root / 'build' / 'item_config.yaml').exists()

    def input_help(self):
        # item: /path/to/item(under item) >_
        # else: /path/to/non-item >_
        if self.is_item():
            return imp(f'{self.item_root}') + sec('(under item)') + imp('> ')
        else:
            return imp(f'{self.item_root} > ')

    def cd(self, *command):
        new_dir = command[0]
        self.item_root = Path(new_dir)

    def help(self, *command):
        # show the help message
        if len(command) == 0:
            command = 'None'
        else:
            command = '_'.join([str(c) for c in command])
        try:
            print(self.global_config['__help_text__'][f'help_{command}'])
        except:
            print(f"there is not tag called 'help_text'/'help_{command}'")

    def _get_valid_file(self, path):
        # get the exist file's path
        print(sec('please enter the file name following:'))
        get_parent_dir_ls(path)
        input_ = input(sec('(enter ?q to leave)> '))
        if (path / input_).exists():
            return input_
        else:
            return self._get_valid_file(path)