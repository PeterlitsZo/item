import yaml
from pathlib import Path
# from .item import main

yaml.warnings({'YAMLLoadWarning': False})

def _data(yaml_file:Path):
    data = yaml.safe_load(yaml_file.read_text())
    return data

def _is_sep_str(string:str):
    if string[:2] == '__' and string[-2:] == '__':
        return True
    else:
        return False

def config(global_yaml_Path, local_yaml_Path, command, item_path):
    global_yaml = _data(global_yaml_Path)
    local_yaml = {}

    for gy in global_yaml.copy():
        if not _is_sep_str(gy):
            local_yaml[gy] = global_yaml.pop(gy)

    for gy in global_yaml:
        if gy == '__init__':
            data = global_yaml['__init__'][command]
            for d in data.copy():
                if not _is_sep_str(d):
                    local_yaml[d] = data.pop(d)
            for d in data.copy():
                    if d == '__new_dir__':
                        for dir_path in data.pop('__new_dir__'):
                            dir_path = item_path / dir_path
                            dir_path.mkdir(exist_ok = True)
                    elif d == '__file__':
                        for file_path in data.pop('__file__'):
                            file_path = item_path / file_path
                            (item_path / file_path).touch(exist_ok=True)
                    elif d == '__command__':
                        for command in data.pop('__command__'):
                            if command[0][0] == '!':
                                command[0] = command[0][1:]
                                subprocess.run(command, cwd=item.item_root)
        else:
            raise KeyError(f"I can't deal with the 'key' in global yaml file: '{gy}'")

    local_yaml_Path.touch(exist_ok = True)
    local_yaml_Path.write_text(yaml.safe_dump(local_yaml))