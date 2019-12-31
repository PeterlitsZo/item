from pathlib import Path
from .color import imp, sec
from .env import item_env
from .config import item_config

class item_core(item_env):
    def __init__(self):
        super().__init__()

    def init(self, *command):
        # make a current dir be an 'item'
        # self.is_item(): False -> True
        if len(command) > 1:
            print(f"command is too long, taste as 'init {command}''")
        elif len(command) == 0:
            print(f"init need the case like 'init cpp'")
            return
        command = command[0]

        if not self.is_item():
            self.config_by_lang(command)
        else:
            print(imp('you are already are in inited item, I can\'t init it twice'))

    def have_command(self, command):
        return (command in self.local_config) or (comand in self.global_config)

    def run_command(self, *command):
        '''only use command[0] -- now'''
        command = command[0]

    def cd(self, *command):
        new_dir = command[0]
        self.cd(new_dir)

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

    def config_by_lang(self, lang):
        self.global_config >> self.local_config

        lang_config = self.global_config['__init__'][lang]
        lang_config >> self.local_config

        for dir_path in lang_config['__new_dir__']:
            (self.path / dir_path).mkdir(exist_ok = True)
        for file_path in lang_config['__file__']:
            (self.path / file_path).touch(exist_ok = True)
        for command in lang_config['__command__']:
            if command[0][0] == '!':
                        command[0] = command[0][1:]
                        subprocess.run(command, cwd=self.path)

        self.local_config.write()