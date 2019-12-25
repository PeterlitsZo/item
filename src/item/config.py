from ruamel.yaml import YAML
import re
from pathlib import Path

_yamler = YAML()

class item_config(object):
    def __init__(self, yaml_file:Path = None, *, data:dict = {}):
        self.yaml_file_path = yaml_file
        self.is_sub_config = False if yaml_file else True

        if (not self.is_sub_config) and self.yaml_file_exists():
            self.data = _yamler.load(self.yaml_file_path)
            # if there is a yaml file, it must be a dict
            assert isinstance(self.data, dict)
        else:
            self.data = data

        self._reload_key_set()

    def _reload_key_set(self):
        self.sep_key_set = {key for key in self.data if self._is_spe_str(key)}
        self.var_key_set = {key for key in self.data if self._is_var_str(key)}
        self.com_key_set = {key for key in self.data if self._is_com_str(key)}

    # ----------------------------------------------------
    # 1. __special__
    @classmethod
    def _is_spe_str(cls, string:str):
        # return True if the string have farmat like:
        # __init__, __config__
        # those meaning it is a Special String Key.
        return bool(re.match(r'__.*__', string))

    # 2. _variable_
    @classmethod
    def _is_var_str(cls, string:str):
        # return True if the string have farmat like:
        # _help_text_, _helper_color_
        # those mean it is a Variable String Key.
        return bool(re.match(r'_(?!_).*[^_]_', string))

    # 3. else, it mean it is a gourp of commands.
    @classmethod
    def _is_com_str(cls, string:str):
        # return True if the string have farmat like:
        # _help_text_, _helper_color_
        # those mean it is a Variable String Key.
        return not (cls._is_var_str(string) or cls._is_spe_str(string))
    # ------------------------------------------------------

    def __rshift__(self, other):
        """return self >> other
        
        move all 'variable' and 'command' from self to other"""
        for key in self.var_key_set | self.com_key_set:
            other.data[key] = self.data[key]

    def __or__(self, other):
        """return self | other

        if self.data is emtry(set()), return other,
        else if data's len >= 1, then return self"""
        if len(self.data) == 0:
            return other
        else:
            return self

    def __repr__(self):
        data_yaml_format = ''
        _yamler.dump(self.data, data_yaml_format)
        return f'<item_config on file:{self.yaml_file_path}>:\n' + \
               data_yaml_format

    def __getitem__(self, index) -> 'item_config(dict)' or 'list or str ...':
        # return sub_config
        try:
            if isinstance(self.data[index], dict):
                return item_config(data = self.data[index])
            else:
                return self.data[index]
        except:
            # if there is not 'index' key in data
            # return null sub_config
            return item_config(data={})

    def __iter__(self) -> 'iterable':
        return (self[index] for index in self.data)

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

    # ------------------------------------------------
    def write(self):
        self._touch_yaml()
        _yamler.dump(self.data, self.yaml_file_path)

    def yaml_file_exists(self):
        return self.yaml_file_path.exists()