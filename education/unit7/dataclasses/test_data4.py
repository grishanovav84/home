from dataclasses import dataclass
 
@dataclass
class Person:
    name: str
    age: int
 
    def say_hello(self):
        print(f"{self.name} says hello")
 
 
tom = Person("Tom", 38)
tom.say_hello()     # Tom says hello