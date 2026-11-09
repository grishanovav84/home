class Person:
     type = "Person"
     def __init__(self, name):
         self.name = name
 
 
tom = Person("Tom")
bob = Person("Bob")
print(tom.type)     # Person
print(bob.type)     # Person
 
# изменим атрибут класса
Person.type = "Class Person"
print(tom.type)     # Class Person
print(bob.type)     # Class Person


class Person2:
    name = "Undefined"
 
    def print_name(self):
        print(self.name)
 
 
tom = Person2()
bob = Person2()
tom.print_name()    # Undefined
bob.print_name()    # Undefined
 
bob.name = "Bob"
bob.print_name()    # Bob
tom.print_name()    # Undefined


class Person3:
    __type = "Person3"
 
    @staticmethod
    def print_type():
        print(Person3.__type)
 
 
Person3.print_type()     # Person - обращение к статическому методу через имя класса
 
tom = Person3()
tom.print_type()     # Person - обращение к статическому методу через имя объекта