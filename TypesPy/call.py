# Callable is used to represent objects e.g functions
from typing import Callable

# High order functions

def apply_function(x: int, func: Callable[[int], int]) -> int:
    return func(x)

def square(x: int) -> int:
    return x * x

result = apply_function(5, square)
print(result)  # Output: 25