#importing sequence
from typing import Sequence

#List, tuples and strings are called sequences because they can be indexed. 
name: Sequence = 'I love milk..'
my_hobbies: Sequence = ['Coding', 'Sleeping', 'Eating']
my_bmi: Sequence = (5.7,56)

#no errors 

my_age: Sequence = 23
#error here

my_hobbies: list[Sequence] = ['Coding', 'Sleeping', 'Eating', 23]

class School:
    def __init__(self, name: Sequence, form: Sequence[int]) -> None:
        self.name = name
        self.form = form
        
my_school: School = School('Brighton', [1,2,3,4])
print(f"My school name is {my_school.name} and I am in form {my_school.form[3]}")

class company:
    def __init__(self, name: Sequence, products: Sequence[Sequence]) -> None:
        self.name = name
        self.products = products

my_company: company = company('Brighton', [['Iphone', 2000], ['Ipad', 3000]])
print(f"My company name is {my_company.name} and I sell {my_company.products[1][0]}")
    

