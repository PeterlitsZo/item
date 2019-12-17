from core import item
import subprocess
from sys import argv
from color import sec

def deal_with_command(item, command:list):
    if command == []:
        return 'continue'
    try:
        if   command[0] in ('help', 'h', '--help', '-h'):
            item.help(*command[1:])
        elif command[0] in ('init', 'i'):
            item.init(*command[1:])
        elif command[0] in ('run', 'r'):
            item.run(*command[1:])
        elif command[0] in ('make', 'm'):
            item.make(*command[1:])
        
        elif command[0] in ('exit', 'e', 'quit', 'q'):
            return 'break'
        elif command[0][0] == '!':
            subprocess.run(command[0][1:], cwd=item.item_root)
            print()

        else:
            print(imp(f"no command '{command[0]}', enter 'h' for help\n"))
    except:
        print(imp('[ERROR] something error has happend\n'))


if __name__ == '__main__':
    item = item()

    if len(argv) > 1:
        # use item like: '$ item init'
        deal_with_command(item, argv[1:])

    else:
        # use item like: '$ item'
        #                '/path/of/cwd > init'
        print(sec("cpp_bot:\nenter 'help' or 'h' for help"))
        while True:
            result = deal_with_command(item, input(item.input_help()).split())
            if result == 'break': break
            if result == 'continue': continue