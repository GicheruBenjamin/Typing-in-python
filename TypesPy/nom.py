
#Int for full numbers. 
axe:int = 33
ace:int = 45.22
doll:int = "Graphics"
#float for decimal number or those that have a period.
ba:float = 3.14
be:float = 77
bin:float = "Waters"
#String for characters or a sequence of characters.
cha:str = "Beautiful"
che:str = 44.9
cho:str = 201


#5 errors in this file 2 int, 1 float and 2 str 
class Girl:
    def __init__(self,name: str,isBeautiful: bool):
        self.name = name
        self.isBeautiful = isBeautiful

myclassmate: Girl = Girl("Annet", True)
print(f"My classmate is called {myclassmate.name} and if you ask me if she is beautiful I wuld yes it is {myclassmate.isBeautiful}")






