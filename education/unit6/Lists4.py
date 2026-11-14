
# Проекция списка

numbers = [ 1, 2, 3, 4, 5]
 
def square(number): return number * number
 
result = map(square, numbers)
 
for n in result: print(n, end=" ")      # 1 4 9 16 25

# lambda

numbers2 = [ 1, 2, 3, 4, 5]
 
result = map(lambda n: n * n, numbers2)
 
for n in result: print(n, end=" ")      # 1 4 9 16 25


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
         
people = [ Person("Tom", 38), Person("Kate", 31), Person("Bob", 42), 
        Person("Alice", 34),  Person("Sam", 25) ]
 
# получаем из Person строку с именем
view = map(lambda p: p.name, people)
  
for person in view:
    print(person)

# Минимальное и максимальное значения

numbers3 = [9, 21, 12, 1, 3, 15, 18]
print(min(numbers3))     # 1
print(max(numbers3))     # 21    


# Копирование списков

people1 = ["Tom", "Bob", "Alice"]
people2 = people1
people2.append("Sam")   # добавляем элемент во второй список

# people1 и people2 указывают на один и тот же список
print(people1)   # ["Tom", "Bob", "Alice", "Sam"]
print(people2)   # ["Tom", "Bob", "Alice", "Sam"]


# чтобы происходило копирование элементов, но при этом переменные указывали на разные списки, можно использовать метод copy()

people3 = ["Tom", "Bob", "Alice"]
people4 = people3.copy()    # копируем элементы из people1 в people2
people4.append("Sam")   # добавляем элемент ТОЛЬКО во второй список
# people1 и people2 указывают на разные списки
print(people3)   # ["Tom", "Bob", "Alice"]
print(people4)   # ["Tom", "Bob", "Alice", "Sam"]


# Соединение списков
people5 = ["Tom", "Bob", "Alice"]
people6 = ["Tom", "Sam", "Tim", "Bill"]
people7 = people5 + people6
print(people7)   # ["Tom", "Bob", "Alice", "Tom", "Sam", "Tim", "Bill"]


# Списки списков


people8 = [
    ["Tom", 29],
    ["Alice", 33],
    ["Bob", 27]
]
 
print(people8[0])         # ["Tom", 29]
print(people8[0][0])      # Tom
print(people8[0][1])      # 29



people9 = [
    ["Tom", 29],
    ["Alice", 33],
    ["Bob", 27]
]
 
# создание вложенного списка
person = list()
person.append("Bill")
person.append(41)

# добавление вложенного списка
people9.append(person)
 
print(people9[-1])         # ["Bill", 41]
 
# добавление во вложенный список
people9[-1].append("+79876543210")
 
print(people9[-1])         # ["Bill", 41, "+79876543210"]
 
# удаление последнего элемента из вложенного списка
people9[-1].pop()
print(people9[-1])         # ["Bill", 41]
 
# удаление всего последнего вложенного списка
people9.pop(-1)
 
# изменение первого элемента
people9[0] = ["Sam", 18]
print(people9)            # [ ["Sam", 18], ["Alice", 33], ["Bob", 27]]