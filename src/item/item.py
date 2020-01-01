from .core import item_core
import sys
from .color import sec, imp
import traceback

def deal_with_command(item, command:list):
    if command == []:
        return 'continue'
    try:
        return item.run(command)
    except Exception as e:
        print(imp('----[ERROR] something error has happend:'))
        exc_str = traceback.format_exc().split('\n')
        print(*['    ' + s for s in exc_str[:-1]], sep='\n', end='')
        print(imp('\n----[END ERROR]'))

def main():
    argv = sys.argv[1:]
    item = item_core()

    if len(argv) >= 1:
        # use item like: '$ item init'
        deal_with_command(item, argv)

    else:
        # use item like: '$ item'
        #                '/path/of/cwd > init'
        print(sec("item:\nenter 'help' or 'h' for help\n"))
        while True:
            helper = '(under item)' if item.is_item_root() else ''
            helper = item.path.helper(helper)
            print(helper, end='')
            result = deal_with_command(item, input().split())
            if result == 'break': break
            if result == 'continue': continue
            print()