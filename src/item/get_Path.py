from pathlib import Path
from .color import imp, sec

def get_parent_dir_ls(dir_str):
    dir_path = Path(dir_str)

    for file_ in list(dir_path.iterdir()):
        print(sec(file_.name))