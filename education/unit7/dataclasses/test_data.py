# class Person:
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
 
# tom = Person("Tom", 38)
# print(f"Name: {tom.name}  Age: {tom.age}")      # Name: Tom  Age: 38


from dataclasses import dataclass
 
@dataclass
class Person:
    name: str
    age: int
 
tom = Person("Tom", 38)
print(f"Name: {tom.name}  Age: {tom.age}")      # Name: Tom  Age: 38
