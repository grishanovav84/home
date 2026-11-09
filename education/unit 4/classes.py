class Person:
 
    def __init__(self, name, age):
        self.name = name        # имя человека
        self.age = age          # возраст человека
 
 
tom = Person("Tom", 22)
 
tom.company = "Microsoft"
print(tom.company)  # Microsoft



class Person2:       # определение класса Person
    def say(self, message):     # метод 
        print(message)
 
tom = Person2()
tom.say("Hello")    # Hello



class Person3:
 
    def __init__(self, name, age):
        self.name = name        # имя человека
        self.age = age          # возраст человека
     
    def display_info(self):
        print(f"Name: {self.name}  Age: {self.age}")
 
 
tom = Person3("Tom", 22)
tom.display_info()      # Name: Tom  Age: 22
 
bob = Person3("Bob", 43)
bob.display_info()      # Name: Bob  Age: 43



class Person4:
  
    def __init__(self, name):
        self.name = name
        print("Создан человек с именем", self.name)
     
    def __del__(self):
        print("Удален человек с именем", self.name)
  
tom = Person4("Tom1")




class Person5:
  
    def __init__(self, name):
        self.name = name
        print("Создан человек с именем", self.name)
     
    def __del__(self):
        print("Удален человек с именем", self.name)
  
 
def create_person():
    tom = Person5("Tom2")
     
create_person()
print("Конец программы")