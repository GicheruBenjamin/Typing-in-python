# Callable is used to represent objects e.g functions
from typing import Callable

# High order functions

def apply_function(x: int, func: Callable[[int], int]) -> int:
    return func(x)

def square(x: int) -> int:
    return x * x

result = apply_function(5, square)
print(result)  


#Callbacks


def process_data(data: list[int], callback: Callable[[int], None]) -> None:
    for item in data:
        callback(item)

def print_item(x: int) -> None:
    print(x)

process_data([1, 2, 3], print_item)

class MyClass:
    def __init__(self, callback: Callable[[], None]):
        self.callback = callback

    def do_something(self) -> None:
        self.callback()

def my_callback() -> None:
    print("Callback called!")

obj = MyClass(my_callback)
obj.do_something() 