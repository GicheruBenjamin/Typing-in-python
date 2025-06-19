
'''
Classes that are being used s types and not objects 
for validity and clarity
'''

from typing import Callable

# custom.py

class TypeValidator:
    expected_type = object
    def __new__(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f"Expected {cls.expected_type}, got {type(value)}")
        return value

class String(TypeValidator):
    expected_type = str

class Integer(TypeValidator):
    expected_type = int

class Float(TypeValidator):
    expected_type = float

class Boolean(TypeValidator):
    expected_type = bool

class List(TypeValidator):
    expected_type = list

class Dict(TypeValidator):
    expected_type = dict

class Function(TypeValidator):
    expected_type = Callable
    