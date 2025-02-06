

''' This module demonstrates the Call type '''
from typing import Callable


def call(func: Callable)->Callable:
   ## try and catch if the function is callable
   try:
       func()
   except TypeError:
       return func
   else:
       return func
