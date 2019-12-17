try:
    import colored
except:
    class colored(object):
        pass
    colored.fg = lambda x: ''
    colored.attr = lambda x: ''
        
# -------------------------------------------------------------------------------------------
important_color = '#ffaaaa'
secondary_color = '#ffff88'

def c(text, color):
    """meaning: color"""
    return colored.fg(color) + text + colored.attr(0)

def imp(*important_text):
    """meaning: important"""
    result_text = [str(it) for it in important_text]
    result_text = ' '.join(result_text)
    return c(result_text, important_color)

def sec(*less_important_text):
    """meaning: less important(secondary)"""
    result_text = [str(lit) for lit in less_important_text]
    result_text = ' '.join(result_text)
    return c(result_text, secondary_color)