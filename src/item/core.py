from pathlib import Path
from .color import imp, sec
from .get_Path import get_parent_dir_ls
from .config import item_config

class item():
    def __init__(self):
        self.item_root = Path.cwd()
        self.local_config = item_config(self.item_root / 'build' / 'item_config.yaml')
        self.global_config = item_config(Path(__file__).parent / 'global_item_config.yaml')

    def _reload_local_config(self):
        self.local_config = item_config(self.item_root / 'build' / 'item_config.yaml')

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
            self.config_by_lang(command)

        else:
            print(imp('you are already are in inited item, I can\'t init it twice'))

    def is_item(self):
        # if there is 'item_config.yaml' in dir './build',
        # then it is a 'item'
        return self.local_config.yaml_file_exists()

    def input_help(self):
        # item: /path/to/item(under item) >_
        # else: /path/to/non-item >_
        if self.is_item():
            return imp(f'{self.item_root}') + sec('(under item)') + imp('> ')
        else:
            return imp(f'{self.item_root} > ')

    def cd(self, *command):
        new_dir = command[0]
        if new_dir[0] == '.':
            self.item_root = Path(self.item_root / new_dir)
        else:
            self.item_root = Path(new_dir)
        self._reload_local_config()

    def help(self, *command):
        # show the help message
        if len(command) == 0:
            command = 'None'
        else:
            command = '_'.join([str(c) for c in command])
        try:
            print(self.global_config['_help_text_'][f'help_{command}'])
        except:
            print(f"there is not tag called '_help_text_'/'help_{command}'")

    def _get_valid_file(self, path):
        # get the exist file's path
        print(sec('please enter the file name following:'))
        get_parent_dir_ls(path)
        input_ = input(sec('(enter ?q to leave)> '))
        if (path / input_).exists():
            return input_
        else:
            return self._get_valid_file(path)

    def config_by_lang(self, lang):
        self.global_config >> self.local_config

        lang_config = self.global_config['__init__'][lang]
        lang_config >> self.local_config

        for dir_path in lang_config['__new_dir__']:
            (self.item_root / dir_path).mkdir(exist_ok = True)
        for file_path in lang_config['__file__']:
            (self.item_root / file_path).touch(exist_ok = True)
        for command in lang_config['__command__']:
            if command[0][0] == '!':
                        command[0] = command[0][1:]
                        subprocess.run(command, cwd=self.item_root)

        self.local_config.write()