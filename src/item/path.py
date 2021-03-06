from pathlib import Path
from .color import sec, imp
import os

class item_path(os.PathLike):
    '''
    which is suppose by this class:
    1.  __truediv__ (op '/')
    2.  ls(path = None)
    3.  cd(path)
    4.  helper(string = '')
    5.  get_vails_file(path = '')

    which is suppose by the method __getattr__:
    (use self.path._attr_ to make it)

    --------------------(    from Path     )--------------------
    ----<<< method >>>------------------------------------------
    1.  absolute        2.  chmod           3.  exists
    4.  glob            5.  group           6.  is_block_device
    7.  is_char_device  8.  is_dir          9.  is_fifo
    10. is_file         11. is_mount        12. is_socket
    13. iterdir         14. lchmod          15. link_to
    16. lstat           17. mkdir           18. open
    19. owner           20. read_bytes      21. read_text
    22. rename          23. replace         24. resolve
    25. rglob           26. rmdir           27. samefile
    28. stat            29. symlink_to      30. touch
    31. unlink          32. write_bytes     33. write_text

    --------------------(  from PathPure   )--------------------
    ----<<< method >>>------------------------------------------
    34. as_posix        35. as_uri          36. is_absolute
    37. is_reserved     38. joinpath        39. match
    40. relative_to     41. with_name       42. with_suffix
    ----<<< properties >>>--------------------------------------
    1.  anchor          2.  drive           3.  name
    4.  parent          5.  parents         6.  parts
    7.  root            8.  stem            9.  suffix
    10. suffixes

    how can I use those attr?
    use 'from pathlib import Path', then enter 'help(Path._attr_)'

    need help:
    is there any solutiones better than this?
    i just want to make the class be the subclass, but the class
    'Path' is a mateclass instead of common class.
    '''
    def __init__(self, path = None):
        self.path = Path.cwd() if path == None else Path(path)

    def __getattr__(self, attr):
        return object.__getattribute__(self.path, attr)

    def __fspath__(self):
        return str(self)

    def __str__(self):
        return str(self.path)

    def __repr__(self):
        return repr(self.path)

    def __truediv__(self, pathlike):
        return item_path(self.path / pathlike)

    def _tab_doc(self, iterable_of_strs) -> str:
        import re
        result = '  \t'.join(list(iterable_of_strs)).expandtabs(4)
        output_list = []

        end_index = [end.end() for end in re.finditer(r'\S\s', result)]
        begin_index = [begin.start() for begin in re.finditer(r'\s\S', result)]
        begin_flag = 0
        while True:
            if len(result) - begin_flag < 80:
                output_list.append(result)
                return '\n'.join(output_list) + '\n'
            else:
                end_flag = max([end for end in end_index if end < begin_flag+80])
                output_list.append(result[begin_flag:end_flag])
                print(begin_flag, end_flag)
                begin_flag = min([begin for begin in begin_index if begin >= end_flag])

    def ls(self, path = None):
        path = self.path if path == None else Path(path)
        ls_str_list = []
        for file in list(path.iterdir()):
            print_string = sec(file.name+'/') if file.is_dir() else file.name
            ls_str_list.append(print_string)
        print('  \t'.join(str(res) for res in ls_str_list)) if len(ls_str_list) != 0 else print(sec('[INFO]' + 'there is not file'))
    
    def cd(self, path:str or Path):
        '''will charge the self.path'''
        path = (self.path / path).resolve()
        if path.is_dir():
            self.path = path
        else:
            print(imp('[ERROR]'), 'no such file or directory')

    def helper(self, string = ''):
        # item: /path/to/item(_string_) >_
        return imp(f'{self.path}') + sec(string) + imp(' > ')

    def get_vaild_file(self, path = ''):
        path = self.path / path
        while True:
            print(sec('please enter the file name following:'))
            self.ls(path)
            input_ = input(sec('(enter ?q to leave)> '))
            if input_ == '?q':
                break
            elif (path / input_).exists():
                return (path / input_)
            else:
                print(f'there is no file named \'{input_}\'')
                continue