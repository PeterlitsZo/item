import subprocess
from .color import imp, sec

class item_commander(object):
    def __init__(self, item_env):
        self.cwd = item_env.path
        self.env = item_env

    def __call__(self, iterable_or_str):
        if isinstance(iterable_or_str, str):
            command = iterable_or_str.split()
        else:
            command = iterable_or_str

        return self.run(command)

    def run(self, command: 'iterable'):
        if command[0][0] == '!':
            # like: '!vim' or '!git status'
            command[0] = command[0][1:]
            return self.run_external(command)
        elif command[0] in ('help', 'h', '--help', '-h'):
            self.help(*command[1:])
        elif command[0] in ('init'):
            self.init(*command[1:])
        elif command[0] in ('cd'):
            self.cd(*command[1:])
        elif command[0] in ('ls'):
            self.cwd.ls()
        
        elif command[0] in ('exit', 'quit', 'q'):
            return 'break'

        elif self.have_command(command[0]):
            self.run_command(command)

        else:
            print(imp('[ERROR]'), 'no command', imp(f"'{command[0]}'") + ',', 'enter', imp("'h'"), 'for help')

    def run_external(self, command:'iterable'):
        print(sec(f'run external command:{command} in {self.cwd}'))
        print('--------------------------------------------------')
        subprocess.run(command, cwd=self.cwd)

    def init(self, *command):
        # make a current dir be an 'item'
        # self.is_item(): False -> True
        if len(command) > 1:
            print(f"command is too long, taste as 'init {command}''")
        elif len(command) == 0:
            print(f"init need the case like 'init cpp'")
            return
        command = command[0]

        if not self.env.is_item_root():
            self.config_by_lang(command)
        else:
            print(imp('you are already are in inited item, I can\'t init it twice'))

    def have_command(self, command):
        return (command in self.env.local_config) or (command in self.env.global_config)

    def run_command(self, *command):
        '''only use command[0] -- now'''
        command = command[0]

    def cd(self, *command):
        new_dir = command[0]
        self.cwd.cd(new_dir)
        self.env._reload_local_config()

    def help(self, *command):
        # show the help message
        if len(command) == 0:
            command = 'None'
        else:
            command = '_'.join([str(c) for c in command])
        try:
            print(self.env.global_config['_help_text_'][f'help_{command}'])
        except:
            print(f"there is not tag called '_help_text_'/'help_{command}'")

    def config_by_lang(self, lang):
        self.env.global_config >> self.env.local_config

        lang_config = self.env.global_config['__init__'][lang]
        lang_config >> self.env.local_config

        for dir_path in lang_config['__new_dir__']:
            (self.cwd / dir_path).mkdir(exist_ok = True)
        for file_path in lang_config['__file__']:
            (self.cwd / file_path).touch(exist_ok = True)
        for command in lang_config['__command__']:
            self.run(command)

        self.env.local_config.write()