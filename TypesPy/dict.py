

from typing import dict , Sequence,list , Any


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


my_work_today: dict[any] = {
    "task": "Code",
    "time": 1,
    "priority": 1,
    "completed": False,
    "notes": None,
    "dependencies": []
}


print(f"My work oday is to m${my_work_today["task"]} and it is my priority number ${my_work_today["priority"]} ")