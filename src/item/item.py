from .core import item as item_class
import subprocess
from sys import argv
from .color import sec, imp

def deal_with_command(item, command:list):
    if command == []:
        return 'continue'

    try:
        if   command[0] in ('help', 'h', '--help', '-h'):
            item.help(*command[1:])
        elif command[0] in ('init'):
            item.init(*command[1:])
        elif command[0] in ('cd'):
            item.cd(*command[1:])
        
        elif command[0] in ('exit', 'quit', 'q'):
            return 'break'
        elif command[0][0] == '!':
            command[0] = command[0][1:]
            subprocess.run(command, cwd=item.item_root)

        else:
            print(imp(f"no command '{command[0]}', enter 'h' for help"))
    except Exception as e:
        print(imp('[ERROR] something error has happend:'), e, imp('[END ERROR]'),
              sep = '\n')

def main(*argv):
    item = item_class()

    if len(argv) >= 1:
        # use item like: '$ item init'
        deal_with_command(item, argv)

    else:
        # use item like: '$ item'
        #                '/path/of/cwd > init'
        print(sec("cpp_bot:\nenter 'help' or 'h' for help"))
        while True:
            result = deal_with_command(item, input(item.input_help()).split())
            if result == 'break': break
            if result == 'continue': continue
            print()