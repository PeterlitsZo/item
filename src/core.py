from pathlib import Path
from color import imp, sec
from get_Path import get_parent_dir_ls

class item():
    def __init__(self):
        self.item_root = Path.cwd()
        self.dir_ = {dir_name: self.item_root / dir_name for dir_name in ('bin', 'src', 'include', 'build')}

    def init(self):
        if not self.is_item:
            for dir_name in self.dir_:
                self.dir_[dir_name].mkdir(exist_ok = True)
                print(dir_name, 'was built right now')
            (self.dir_['build'] / 'cpp_bot_config.yaml').touch(exist_ok=True)
            print("config file in dir 'build' is built right now")
            print()
        else:
            print(imp('you are already are in inited item, I can\'t init it twice\n'))

    def is_item(self):
        return (self.dir_['build'] / 'item_config.yaml').exists()

    def make(self, file_name:str = None):
        if file_name == None:
            self.make(self._get_valid_file(self.dir_['src']))
        elif (self.dir_['src'] / file_name).exists():
            subprocess.run(['gcc', self.dir_['src'] / file_name, '-o', (self.dir_['bin'] / file_name).with_suffix('')])
        else:
            self.make(None)

    def run(self, file_name:str = None):
        if file_name == None:
            self.run(self._get_valid_file(self.dir_['bin']))
        elif (self.dir_['bin'] / file_name).exists():
            subprocess.run([self.dir_['bin'] / file_name])
        else:
            self.run(None)

    def input_help(self):
        if self.is_item():
            input_help = imp(f'{self.item_root}') + sec('(cpp_bot_item)') + imp('> ')
        else:
            input_help = imp(f'{self.item_root} > ')
        return input_help

    def help(self):
        help_txt = Path(__file__).parent / 'help.txt'
        print(help_txt.open().read())

    def _get_valid_file(self, path):
        print(sec('please enter the file name following:'))
        get_parent_dir_ls(path)
        input_ = input(sec('(enter ?q to leave)> '))
        if (path / input_).exists():
            return input_
        else:
            return self._get_valid_file(path)