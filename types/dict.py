
''' This module demonstrates the Dict type '''
from typing import Dict


def dict_(d: Dict)->Dict:
    # Allowing only dict types to be passed
    try:
        d['key']
    except KeyError:
        return d
    else:
        return d  
        