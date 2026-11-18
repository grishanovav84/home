from dataclasses import dataclass
 
@dataclass
class Person:
    name: str
    age: int = 18
 
 
tom = Person("Tom", 38)
print(tom)              # Person(name="Tom", age=38)
 
bob = Person("Bob")
print(bob)              # Person(name="Bob", age=18)