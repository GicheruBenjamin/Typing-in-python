# Callable is used to represent objects e.g functions
from typing import Callable

def display_operation_results(x: int, op: Callable[[int], int]) -> None:
    print(op(x))

def square(x: int) -> int:
    return x * x

display_operation_results(22, square) #output 484