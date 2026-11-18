from dataclasses import dataclass
 
@dataclass(unsafe_hash=True, order=True)
class Person:
    name: str
    age: int
    def __repr__(self):
        return f"Person. Name: {self.name}  Age: {self.age}"
 
 
tom = Person("Tom", 38)
print(tom.__hash__())   # -421667297069596717
print(tom)              # Person. Name: Tom  Age: 38