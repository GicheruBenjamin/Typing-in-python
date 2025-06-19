
'''Working with Lists'''
from typing import List

def list_(l: List)->List:
    # Allowing only list types to be passed
    try:
        l[0]
    except IndexError:
        return l
    else:
        return l