

''' This module demonstrates the Call type '''
from typing import Callable


def call(func: Callable)->Callable:
    ''' This function takes a function and returns a function '''
    return func


def call2(func: Callable)->Callable:
    ''' This function takes a function and returns a function '''
    return func 
