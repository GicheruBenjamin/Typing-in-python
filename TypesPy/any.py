
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

#print(result + " is the sum of 1 and 2") # This will cause type error

#Error from add_numbers func

def unknown() -> Any:
    return lambda: print("I am an unknown function")

unknown()
class Event:
    no_of_parties: int = 0
    def __init__(self, name: str, no_of_people: int):
        self.name = name
        self.no_of_people = no_of_people
        total_parties:int = Event.no_of_parties
        Event.no_of_parties = total_parties + 1

my_event: Event = Event("Birthday", 10)
print(Event.no_of_parties)
my_brothers: list[Any] = [Event("Birthday", 10), Event("Birthday", 10), Event("Birthday", 10)]
print(Event.no_of_parties)