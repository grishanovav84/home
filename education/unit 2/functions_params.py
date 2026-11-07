def say_hello(name):
    print(f"Hello, {name}")
 
say_hello("Tom")
say_hello("Bob")
say_hello("Alice")



def print_person(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")
 
 
print_person("Tom", 37)



def say_hello2(name="Tom"):
    print(f"Hello, {name}")
 
 
say_hello2()         # здесь параметр name будет иметь значение "Tom"
say_hello2("Bob")    # здесь name = "Bob"



def print_person2(name, age = 18):
    print(f"Name: {name}  Age: {age}")
 
 
print_person2("Bob")
print_person2("Tom", 37)



def print_person3(name, age):
    print(f"Name: {name}  Age: {age}")
 
 
print_person3(age = 22, name = "Tom")



def print_person4(name, *,  age, company):
    print(f"Name: {name}  Age: {age}  Company: {company}")
 
 
print_person4("Bob", age = 41, company ="Microsoft")    # Name: Bob  Age: 41  company: Microsoft


def print_person5(*,  name, age, company):
    print(f"Name: {name}  Age: {age}  Company: {company}")



def print_person6(name, /, age, company="Microsoft"):
    print(f"Name: {name}  Age: {age}  Company: {company}")
 
 
print_person6("Tom", company="JetBrains", age = 24)     # Name: Tom  Age: 24  company: JetBrains
print_person6("Bob", 41)      



def print_person7(name, /,  age = 18, *, company):
    print(f"Name: {name}  Age: {age}  Company: {company}")
 
 
print_person7("Sam", company ="Google")               # Name: Sam  Age: 18  company: Google
print_person7("Tom", 37, company ="JetBrains")        # Name: Tom  Age: 37  company: JetBrains
print_person7("Bob", company ="Microsoft", age = 42)  # Name: Bob  Age: 42  company: Microsoft           # Name: Bob  Age: 41  company: Microsoft



def sum(*numbers):
    result = 0
    for n in numbers:
        result += n
    print(f"sum = {result}")
 
 
sum(1, 2, 3, 4, 5)      # sum = 15
sum(3, 4, 5, 6)         # sum = 18