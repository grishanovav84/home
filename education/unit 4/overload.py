class Counter:
    def __init__(self, value):
        self.value = value
    
    # переопределение оператора сложения
    def __add__(self, other):
        return Counter(self.value + other.value)
     
counter1 = Counter(5)
counter2 = Counter(15)
counter3 = counter1 + counter2
print(counter3.value)       # 20




class Counter2:
    def __init__(self, value):
        self.value = value
    
    # позволяет установить истинность объект    
    def __bool__(self):
        return self.value > 0
     
def test(counter):
    if counter: print("Counter = True")
    else: print("Counter = False")
     
counter1 = Counter2(3)
test(counter1)              # Counter = True
 
counter2 = Counter2(-3)
test(counter2)              # Counter = False



class Counter3:
    def __init__(self, value):
        self.value = value

    # операторы, которые возвращают значение bool         
    def __gt__(self, other):
        return self.value > other.value
    def __lt__(self, other):
        return self.value < other.value
 
     
counter1 = Counter3(1)
counter2 = Counter3(2)
     
if counter1 > counter2: 
    print("counter1 больше чем counter2")
elif counter1 < counter2:
    print("counter1 меньше чем counter2")
else: 
    print("counter1 и counter2 равны")



class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
         
    def __getitem__(self, prop):
        if prop == "name": return self.__name
        elif prop == "age": return self.__age
        return None
     
tom = Person("Tom", 39)

# операции обращения по индексу
print("Name:", tom["name"])     # Name: Tom
print("Age:", tom["age"])       # Age: 39
print("Id:", tom["id"])         # Id: None



class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # проверка наличия свойства         
    def __contains__(self, prop):
        if prop == "name" or prop == "age": return True
        return False
     
tom = Person2("Tom", 39)

print("name" in tom)        # True
print("id" in tom)          # False