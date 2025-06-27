
from typing import Any, Union, Optional, Literal, Annotated, NamedTuple, Iterable,\
    NewType


# If type is wrong on funcs 
# A str sayin "U put wrong type" 
def _check_type(func)->str:
    if func is TypeError:
        return "TypeError"
    else:
        return "None"

# Any type
def _display(value: Any):
    print(value)

# Union type
def _calculate_price(price: Union[int, float])->float:
    return price * 1.2

# Optional type
def _see_someone(name: str, availability: Optional[str]):
    if availability:
        print(f"Hello {name}, you are available")
    else:
        print(f"Hello {name}, you are not available")

# Literal type
def move(direction: Literal["up", "down", "left", "right"]) -> None:
    print(f"Moving {direction}")


# Annotated
def length(name : Annotated[str,"must be a string"]) -> int:
    return len(name)

# -- Collection types --
# -- List --
def _list(values: list[int]) -> None:
    print(values)

# -- Tuple --
def _tuple(values: tuple[int, str]) -> None:
    print(values)

# -- Set --
def _set(values: set[int]) -> None:
    print(values)

# -- Dict --
def _dict(values: dict[str, int]) -> None:
    print(values)

# -- NamedTuple --
class Person(NamedTuple):
    name: str
    age: int

# Iterable
def _iterable(values: Iterable[int]) -> None:
    print(values)


# ---Function and Generics---

from typing import TypeVar
T = TypeVar('T')

def _generic(values: list[T]) -> None:
    print(values)


# --- Protocols ---
from typing import Protocol
class Shape(Protocol):
    def area(self) -> float:
        pass
    def perimeter(self) -> float:
        pass

class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height
    def area(self) -> float:
        return self.width * self.height
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius
    def area(self) -> float:
        return 3.14 * self.radius * self.radius
    def perimeter(self) -> float:
        return 2 * 3.14 * self.radius
    
# New type 
userId = NewType('userId', int)
def _get_user(user_id: userId) -> None:
    print(user_id)

# --- Type Aliases ---
from typing import TypeAlias
UserId: TypeAlias = int
def _get_user_byid(user_id: UserId) -> None:
    print(user_id)

# --- TypedDict ---
from typing import TypedDict
class User(TypedDict):
    name: str
    age: int
def _get_user_name_age(user: User) -> None:
    print(user)


def main():
    """
    Testing all the types available
    Have several instances where they are correct and others are wrong 
    """
    # Any type
    _display(1)
    _display("Hello")
    _display(True)
    _display([1, 2, 3])
    _display({"name": "John", "age": 30})
    _display(None)
    
    # Union type
    _calculate_price(1)
    _calculate_price(1.5)
    _calculate_price("1.5")# TypeError
    
    # Optional type
    _see_someone("John", None)
    _see_someone("John", "available")
    _see_someone("John", "not available")

    # Literal type
    move("up")
    move("down")
    move("left")
    move("right")
    move("not available")# TypeError

    # Annotated
    length("John")
    length(123)# TypeError

    # List
    _list([1, 2, 3])
    _list([1, "2", 3])# TypeError

    # Tuple
    _tuple((1, 2, 3))
    _tuple((1, "2", 3))# TypeError

    # Set
    _set({1, 2, 3})
    _set({1, "2", 3})# TypeError

    # Dict
    _dict({"name": "John", "age": 30})
    _dict({"name": 30, "age": 30})# TypeError

    # NamedTuple
    Person("John", 30)
    Person(30, "John")# TypeError

    # Iterable
    _iterable([1, 2, 3])
    _iterable("Hello")# TypeError

    # Generics
    _generic([1, 2, 3])
    _generic("Hello")# TypeError

    # Protocols
    Rectangle(1, 1)
    Rectangle(1, "1")# TypeError
    Circle(1)
    Circle("1")# TypeError

    # New type
    _get_user(1)
    _get_user("1")# TypeError

    # Type Aliases
    _get_user_byid(1)
    _get_user_byid("1")# TypeError

    # TypedDict
    _get_user_name_age({"name": "John", "age": 30})
    _get_user_name_age({"name": 30, "age": 30})# TypeError

if __name__ == "__main__":
    main()