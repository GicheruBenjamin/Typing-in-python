

''' Running lambda functions '''

from typing import Callable

def lambda_(func: Callable)->Callable:
    # Allowing only lambda functions to be passed
    try:
        func()
    except TypeError:
        return func
    else:
        return func