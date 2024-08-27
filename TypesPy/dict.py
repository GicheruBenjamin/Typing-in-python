

from typing import dict , Sequence,list


my_hobbies: dict[str, Sequence] = {
    "name": "Alice",
    "hobbies": ["Coding", "Sleeping", "Eating"],
}

print(my_hobbies["hobbies"])

people:dict[str,List[str]] = {
    "friends": ["john", "jane"],
    "family": ["dad", "mom"]
}

print(people["friends"[1]])   
