from ruamel.yaml import YAML
import re
from pathlib import Path
from collections import UserDict

_yamler = YAML()

# ----------------------------------------------------
# 1. __special__
def _is_spe_str(string:str):
    # return True if the string have farmat like:
    # __init__, __config__
    # those meaning it is a Special String Key.
    return bool(re.match(r'__.*__', string))

# 2. _variable_
def _is_var_str(string:str):
    # return True if the string have farmat like:
    # _help_text_, _helper_color_
    # those mean it is a Variable String Key.
    return bool(re.match(r'_(?!_).*[^_]_', string))

# 3. else, it mean it is a gourp of commands.
def _is_com_str(string:str):
    # return True if the string have farmat like:
    # _help_text_, _helper_color_
    # those mean it is a Variable String Key.
    return not (_is_var_str(string) or _is_spe_str(string))
# ------------------------------------------------------


class item_config_base(UserDict):
    def __init__(self, data: dict):
        super().__init__(data)
        self._reload_key_set()

    def _reload_key_set(self):
        self.sep_key_set = {key for key in self if _is_spe_str(key)}
        self.var_key_set = {key for key in self if _is_var_str(key)}
        self.com_key_set = {key for key in self if _is_com_str(key)}

    def __getitem__(self, index):
        data = super().__getitem__(index)
        return item_config_base(data) if isinstance(data, dict) else data


class item_config(item_config_base):
    def __init__(self, yaml_file:Path):
        self.yaml_file_path = yaml_file
        if self.yaml_file_exists():
            super().__init__(_yamler.load(self.yaml_file_path))
        else:
            super().__init__({})

    def __rshift__(self, other):
        """return self >> other
        
        move all 'variable' and 'command' from self to other"""
        for key in self.var_key_set | self.com_key_set:
            other[key] = self[key]

    def __or__(self, other):
        """return self | other

        if self.data is emtry(set()), return other,
        else if data's len >= 1, then return self"""
        if len(self) == 0:
            return other
        else:
            return self

    def __repr__(self):
        return f'<item_config on file:{self.yaml_file_path}>:\n' + \
               super().__repr__(self)

    # -----------------------------------------------------

    def _touch_yaml(self):
        if self.yaml_file_exists():
            for parent_path in reversed(self.yaml_file_path.parents):
                if not parent_path.exists():
                    parent_path.mkdir()
            else:
                self.yaml_file_path.touch()
        else:
            # if there is already a yaml config file:
            return

    # ------------------------------------------------------

    def write(self):
        self._touch_yaml()
        _yamler.dump(self.data, self.yaml_file_path)

    def yaml_file_exists(self):
        return self.yaml_file_path.exists()