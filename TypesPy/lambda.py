 
#Using type hints in a lambda functions
hobby:any =lambda: "I hate java.";print(hobby())
eat: str = lambda food: f"I like {food}."
print(eat("pizza"))

#No errors here
# Can also be used with callable type
great_food: callable = lambda food: print(f"I like {food}.")
great_food("pizza") 
