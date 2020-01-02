try:
    import colored
except:
    class colored(object):
        pass
    colored.fg = lambda x: ''
    colored.attr = lambda x: ''
from collections import UserString, UserList

# -------------------------------------------------------------------------------------------
important_color = '#ffaaaa'
secondary_color = '#ffff88'

class colored_text_base(UserString):
    def __init__(self, text, color=None):
        super().__init__(text)
        self.color = color

    def __str__(self):
        fg = '' if self.color is None else colored.fg(self.color)
        attr = '' if self.color is None else colored.attr(0)
        return fg + self.data + attr

    def __repr__(self):
        return '<colored_text_base: "' + self.__str__() + '">'

    def __add__(self, value):
        value = value if isinstance(colored_text_base) else colored_text_base(value)
        return colored_text(self, value)

class colored_text(UserList):
    def __init__(self, iterable_colored_text_base):
        super().__init__(iterable_colored_text_base)

    def __len__(self):
        return sum(len(ct) for ct in self)

    def __str__(self):
        return ''.join(str(result) for result in self)

    def __repr__(self):
        return '<colored_text: "' + self.__str__() + '">'

    def __add__(self, value):
        if isinstance(value, str):
            self.data.append(colored_text_base(value))
        elif isinstance(value, colored_text_base):
            self.data.append(value)
        elif isinstance(value, colored_text):
            self.data.extend(value)
        return self

    def __radd__(self, value):
        if isinstance(value, str):
            data = colored_text([colored_text_base(value)])
        elif isinstance(value, colored_text_base):
            data = colored_text([value])
        elif isinstance(value, colored_text):
            data = value
        data.exatnd(self)
        return data

    @classmethod
    def text_color(cls, text, color):
        ctb = colored_text_base(text, color)
        return cls([ctb])

def imp(*important_text):
    """meaning: important"""
    result_text = [str(it) for it in important_text]
    result_text = ' '.join(result_text)
    return colored_text.text_color(result_text, important_color)

def sec(*less_important_text):
    """meaning: less important(secondary)"""
    result_text = [str(lit) for lit in less_important_text]
    result_text = ' '.join(result_text)
    return colored_text.text_color(result_text, secondary_color)