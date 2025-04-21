

''' This module demonstrates the Seq type '''
from typing import Sequence

def seq(s: Sequence)->Sequence:
    # Allowing only sequence types to be passed
    try:
        s[0]
    except IndexError:
        return s
    else:
        return s