
from typing import List,Sequence

my_hobbies: List[str] = ["Coding", "Sleeping", "Eating"]
Companies: List[str] = ["Microsoft", "Google", "Apple", "Facebook"]
cars: List[dict[str: str]] = [    {"make": "Toyota", "model": "Corolla", "year": "2015"},    {"make": "Honda", "model": "Civic", "year": "2018"},    {"make": "Ford", "model": "Mustang", "year": "2019"},    {"make": "Chevrolet", "model": "Camaro", "year": "2020"}]
my_tools: List[Sequence] = ['HpLaptop', ['typescript', 'Dart'], 'coffee']
print(f"I use my {my_tools[0]} to code in {my_tools[1][0]and {my_tools[1][1]}} as I take {my_tools[2]}")

print(f"I would love working in {Companies[1]}")
