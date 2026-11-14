# Добавление и удаление элементов

people = ["Tom", "Bob"]
 
# добавляем в конец списка
people.append("Alice")  # ["Tom", "Bob", "Alice"]
# добавляем на вторую позицию
people.insert(1, "Bill")  # ["Tom", "Bill", "Bob", "Alice"]
# добавляем набор элементов ["Mike", "Sam"]
people.extend(["Mike", "Sam"])      # ["Tom", "Bill", "Bob", "Alice", "Mike", "Sam"]
# получаем индекс элемента
index_of_tom = people.index("Tom")
# удаляем по этому индексу
removed_item = people.pop(index_of_tom)     # ["Bill", "Bob", "Alice", "Mike", "Sam"]
# удаляем последний элемент
last_item = people.pop()     # ["Bill", "Bob", "Alice", "Mike"]
# удаляем элемент "Alice"
people.remove("Alice")      # ["Bill", "Bob", "Mike"]
print(people)       # ["Bill", "Bob", "Mike"]
# удаляем все элементы
people.clear()
print(people)       # []


# Проверка наличия элемента
people2 = ["Tom", "Bob", "Alice", "Sam"]
 
if "Alice" in people2:
    people2.remove("Alice")
print(people2)       # ["Tom", "Bob", "Sam"]


# Удаление с помощью del

people3 = ["Tom", "Bob", "Alice", "Sam", "Bill", "Kate", "Mike"]
 
del people3[1]   # удаляем второй элемент
print(people3)   # ["Tom", "Alice", "Sam", "Bill", "Kate", "Mike"]

del people3[:3]   # удаляем  по четвертый элемент не включая
print(people3)   # ["Bill", "Kate", "Mike"]

del people3[1:]   # удаляем  со второго элемента
print(people3)   # ["Bill"]

# Изменение подсписка

nums = [10, 20, 30, 40, 50]
nums[1:4]=[11, 22]
print(nums)     # [10, 11, 22, 50]

# Подсчет вхождений

people4 = ["Tom", "Bob", "Alice", "Tom", "Bill", "Tom"]
 
people_count = people4.count("Tom")
print(people_count)      # 3



# Сортировка

people5 = ["Tom", "Bob", "Alice", "Sam", "Bill"]
 
people5.sort()
print(people5)      # ["Alice", "Bill", "Bob", "Sam", "Tom"]


people6 = ["Tom", "Bob", "Alice", "Sam", "Bill"]
 
people6.sort()
people6.reverse()
print(people6)      # ["Tom", "Sam", "Bob", "Bill", "Alice"]


people7 = ["Tom", "bob", "alice", "Sam", "Bill"]
 
people7.sort()       # стандартная сортировка
print(people7)      # ["Bill", "Sam", "Tom", "alice", "bob"]
 
people7.sort(key=str.lower)  # сортировка без учета регистра
print(people7)      # ["alice", "Bill", "bob", "Sam", "Tom"]


people8 = ["Tom", "bob", "alice", "Sam", "Bill"]
 
sorted_people2 = sorted(people8, key=str.lower)
print(sorted_people2)      # ["alice", "Bill", "bob", "Sam", "Tom"]


# Фильтрация списка

numbers = [-5, -4, -3 ,-2, -1, 0, 1, 2, 3, 4, 5]
 
def condition(number): return number > 1
 
result = filter(condition, numbers)
 
for n in result: print(n, end=" ")      # 2 3 4 5

# lambda
numbers2 = [-5, -4, -3 ,-2, -1, 0, 1, 2, 3, 4, 5]
 
result = filter(lambda n: n > 1, numbers2)
 
for n in result: print(n, end=" ")      # 2 3 4 5


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
         
people = [ Person("Tom", 38), Person("Kate", 31), Person("Bob", 42), 
        Person("Alice", 34),  Person("Sam", 25) ]
 
# фильтрация элементов, у которых age > 33
view = filter(lambda p: p.age > 33, people)
  
for person in view:
    print(f"Name: {person.name} Age: {person.age}")

