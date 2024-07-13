#Optional function arguments:
from typing import Optional

def greet(name: Optional[str] = None) -> None:
    if name is not None:
        print(f"Hello, {name}!")
    else:
        print("Hello!")

greet("Alice") 
greet() 

#Optional return values:
def find_user(username: str) -> Optional[dict]:
    user_found = False  # Assuming this needs to be initialized
    user_data = {}  # Assuming this needs to be initialized
    
    # Code to find user and populate user_found and user_data

    if user_found:
        return user_data
    else:
        return None


result = find_user("alice")
if result is not None:
    print(f"User found: {result['name']}")
else:
    print("User not found")
    
#Optional attributes:
class User:
    def __init__(self, name: str, email: Optional[str] = None):
        self.name = name
        self.email = email

user = User("Alice")
print(f"Name: {user.name}, Email: {user.email}")  
from typing import Optional

user_data: dict[str, Optional[str]] = {
    "name": "Alice",
    "email": None
}

print(f"Name: {user_data['name']}, Email: {user_data['email']}")  

def MakeGreatFood(food: Optional[str] = None) -> None:
    if food is not None:
        print(f"I like {food}.")
    else:
        print("I like pizza.")

MakeGreatFood("pizza")
MakeGreatFood()
