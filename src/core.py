from pathlib import Path
from color import *
from get_Path import get_parent_dir_ls
import subprocess
from functools import wraps

class item():
    def __init__(self):
        try:
            self.item_root = Path(sys.argv[1])
        except:
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
    
    def _get_valid_file(self, path):
        print(sec('please enter the file name following:'))
        get_parent_dir_ls(path)
        input_ = input(sec('(enter ?q to leave)> '))
        if (path / input_).exists():
            return input_
        else:
            return self._get_valid_file(path)

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

if __name__ == '__main__':
    print(sec("cpp_bot:\nenter 'help' or 'h' for help"))
    item = item()

    while True:
        command = input(item.input_help()).split()
        if command == []:
            continue

        try:
            if   command[0] in ('help', 'h'):
                item.help(*command[1:])
            elif command[0] in ('init', 'i'):
                item.init(*command[1:])
            elif command[0] in ('run', 'r'):
                item.run(*command[1:])
            elif command[0] in ('make', 'm'):
                item.make(*command[1:])
            
            elif command[0] in ('exit', 'e', 'quit', 'q'):
                break
            elif command[0][0] == '!':
                subprocess.run(command[1:], cwd=item.item_root.absolute())
                print()

            else:
                print(imp(f"no command '{command[0]}', enter 'h' for help\n"))
        except:
            print(imp('[ERROR] something error has happend\n'))