from pathlib import Path
from .color import imp, sec
from .get_Path import get_parent_dir_ls
from .read_config import data

class item():
    def __init__(self):
        self.item_root = Path.cwd()
        self.dir_ = {dir_name: self.item_root / dir_name for dir_name in ('bin', 'src', 'include', 'build')}
        self.config = data(self.item_root)

    def init(self):
        # make a current dir be a 'item'
        # self.is_item(): False -> True
        if not self.is_item():
            for dir_name in self.dir_:
                self.dir_[dir_name].mkdir(exist_ok = True)
                print(dir_name, 'was built right now')
            (self.dir_['build'] / 'item_config.yaml').touch(exist_ok=True)
            print("config file in dir 'build' is built right now")
        else:
            print(imp('you are already are in inited item, I can\'t init it twice'))

    def is_item(self):
        # if there is 'item_config.yaml' in dir './build',
        # then it is a 'item'
        return (self.dir_['build'] / 'item_config.yaml').exists()

    def make(self, file_name:str = None):
        # from dir './src' to build bin file and then move it to dir 'bin'
        if file_name == None:
            self.make(self._get_valid_file(self.dir_['src']))
        elif (self.dir_['src'] / file_name).exists():
            subprocess.run(['gcc', self.dir_['src'] / file_name, '-o', (self.dir_['bin'] / file_name).with_suffix('')])
        else:
            self.make(None)

    def run(self, file_name:str = None):
        # run the 'bin' file
        if file_name == None:
            self.run(self._get_valid_file(self.dir_['bin']))
        elif (self.dir_['bin'] / file_name).exists():
            subprocess.run([self.dir_['bin'] / file_name])
        else:
            self.run(None)

    def input_help(self):
        # item: /path/to/item(under item) >_
        # else: /path/to/non-item >_
        if self.is_item():
            return imp(f'{self.item_root}') + sec('(under item)') + imp('> ')
        else:
            return imp(f'{self.item_root} > ')

    def help(self):
        # show the help message
        # help_txt = Path(__file__).parent / 'help.txt'
        # print(help_txt.open().read())
        print(self.config['help_text'])

    def _get_valid_file(self, path):
        # get the exist file's path
        print(sec('please enter the file name following:'))
        get_parent_dir_ls(path)
        input_ = input(sec('(enter ?q to leave)> '))
        if (path / input_).exists():
            return input_
        else:
            return self._get_valid_file(path)