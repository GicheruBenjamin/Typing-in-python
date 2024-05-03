
# Any can be used to take all kinds of primitives.
# Can be used when not sure what type u are going to use.

from typing import Any

def process_data(data: Any) -> Any:
    return data


result = process_data(10)  
result = process_data("Hello")  

def add_numbers(x: int, y: int) -> int:
    return x + y

result = add_numbers(1, 2)  

print(result + " is the sum of 1 and 2") # This will cause type error

#Error from add_numbers func