from pathlib import Path
from src.color import imp, sec

def get_parent_dir_ls(dir_str):
    dir_path = Path(dir_str)

    result = list(dir_path.iterdir())
    for i in result:
        output_name = i.name
        print(sec(output_name))
    return result