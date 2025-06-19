

# Get the custom types from ~/custom.py
from app import String, Integer, Float, Boolean, List, Dict , Function

def main():
    # Using the custom types
    person_type = {
        "name": String,
        "age": Integer,
        "height": Float,
        "is_student": Boolean,
        "hobbies": List,
        "friends": Dict
    }

    actions_type = {
        "Dream" : Function,
        "Eat" : Function,
        "Sleep" : Function
    }

    my_friend : person_type = {
        "name": "John",
        "age": 25,
        "height": 1.75,
        "is_student": False,
        "hobbies": ["reading", "running"],
        "friends": {
            "John": "John",
            "Mary": "Mary"
        }
    }

    my_mom : person_type = {
        "name": "Mary",
        "age": 30,
        "height": 1.65,
        "is_student": True,
        "hobbies": ["running", "reading"],
        "friends": {
            "John": "John",
            "Mary": "Mary"
        }
    }

    my_schedule : List = [
        {
            "action": "Eat",
            "time": "10:00"
        },
        {
            "action": "Sleep",
            "time": "12:00"
        },
        {
            "action": "Dream",
            "time": "18:00"
        }
    ]

    def eat(food : String):
        print(f"Eating {food}")

    def sleep(time : Integer):
        print(f"Sleeping for {time} hours")

    def dream(dream : String):
        print(f"Dreaming about {dream}")

    actions_type["Eat"] = eat
    actions_type["Sleep"] = sleep
    actions_type["Dream"] = dream


    print(my_friend)
    print(my_mom)
    print(my_schedule)

    for action in my_schedule:
        print(actions_type[action["action"]](action["time"]))


if __name__ == "__main__":
    main()