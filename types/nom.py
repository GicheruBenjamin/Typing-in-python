

''' This module demonstrates the regular types '''

from typing import int, float, str, bool

def check_type(var):
    try:
        if isinstance(var, int):
            return True
        elif isinstance(var, float):
            return True
        elif isinstance(var, str):
            return True
        elif isinstance(var, bool):
            return True
        else:
            return False
    except ValueError:
        return False
    else:
        return True