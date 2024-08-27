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
    
class SequenceDemo:
    def __init__(self, sequence):
        self.sequence = sequence

    def __len__(self):
        return len(self.sequence)

    def __getitem__(self, index):
        return self.sequence[index]

    def __iter__(self):
        return iter(self.sequence)

    def __contains__(self, item):
        return item in self.sequence

    def __add__(self, other):
        return SequenceDemo(self.sequence + other.sequence)

    def __mul__(self, other):
        return SequenceDemo(self.sequence * other)

    def __repr__(self):
        return f"SequenceDemo({repr(self.sequence)})"

# Create instances of SequenceDemo
sequence1 = SequenceDemo([1, 2, 3])
sequence2 = SequenceDemo(["a", "b", "c"])

# Access elements using indexing
print(sequence1[0])  # Output: 1
print(sequence2[1])  # Output: b

# Iterate over elements
for item in sequence1:
    print(item)  # Output: 1 2 3

# Check if an element is in the sequence
print(3 in sequence1)  # Output: True
print("d" in sequence2)  # Output: False

# Concatenate sequences
sequence3 = sequence1 + sequence2
print(sequence3)  # Output: SequenceDemo([1, 2, 3, 'a', 'b', 'c'])

# Repeat a sequence
sequence4 = sequence1 * 2
print(sequence4)  # Output: SequenceDemo([1, 2, 3, 1, 2, 3])
