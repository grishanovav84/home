
# zip() в Python позволяет объединить элементы из нескольких коллекций (таких как списки, словари, кортежи или строки) в один набор кортежей

names = ["Tom", "Bob", "Sam"]
ages = [41, 46, 35]
 
for user in zip(names, ages):
    print(user)
 
# Консольный вывод
# ("Tom", 41)
# ("Bob", 46)
# ("Sam", 35)



names2 = ["Tom", "Bob", "Sam"]
ages2 = [41, 46, 35]
 
users2 = zip(names2, ages2)
print(users2)        # <zip object at 0x7c2307627c40>
 
for user in users2:
    print(user)



# передаем список с одинм элементом
for tup in zip([5]):
    print(tup)   # (5,)
 
# передаем кортеж с одним элементом
for tup in zip((6,)):
    print(tup)   # (6,)
 
# передаем словарь с одним элементом
for tup in zip({1: "Tom"}):
    print(tup)   # (1,)    


# передаем список с одинм элементом
for tup in zip([5, 6, 7]):
    print(tup)   
 
# Консольный вывод
# (5,)
# (6,)
# (7,)
# 



list1 = [1, 2, 3]
list2 = ["a", "b"]
 
for tup in (zip(list1, list2)):
    print(tup)
 
# Консольный вывод
# (1, "a")
# (2, "b")


# Объединение списков

names = ["Tom", "Bob", "Sam"]
ages = [41, 46, 35]   
 
users = list(zip(names, ages)) 
print(users)        # [("Tom", 41), ("Bob", 46), ("Sam", 35)]
 
for user in users:
    print(user)
 
# Консольный вывод
# ("Tom", 41)
# ("Bob", 46)
# ("Sam", 35)


names2 = ["Tom", "Bob", "Sam"]
ages2 = [41, 46, 35]   
companies2 = ["Sber", "VK", "Yandex"]
 
users2 = list(zip(names2, ages2, companies2)) 
print(users2)        # [("Tom", 41, "Sber"), ("Bob", 46, "VK"), ("Sam", 35, "Yandex")]
 
for user in users2:
    print(user)
 
# Консольный вывод
# ("Tom", 41, "Sber")
# ("Bob", 46, "VK")
# ("Sam", 35, "Yandex")


# Разложение списка кортежей

users = [("Tom", 41), ("Bob", 46), ("Sam", 35)]
 
names, ages = zip(*users)
 
print(names)    # ("Tom", "Bob", "Sam")
print(ages)     # (41, 46, 35)


# Одновременный перебор нескольких список

names = ["Tom", "Bob", "Sam"]
ages = [41, 46, 35]
 
for name, age in zip(names, ages):
    print(f"Name: {name}  Age: {age}")
 
# Консольный вывод
# Name: Tom  Age: 41
# Name: Bob  Age: 46
# Name: Sam  Age: 35


# Создание словарей


keys = ["name", "age", "city"]
values = ["Tom", 41, "Volgograd"]
 
user = dict(zip(keys, values))
print(user)  # {"name": "Tom", "age": 41, "city": "Volgograd"}

# Работа с диапазонами

numbers = range(1, 4)
letters = ["a", "b", "c"]
 
result = list(zip(numbers, letters))
print(result)  # [(1, "a"), (2, "b"), (3, "c")]


# Сравнение элементов в списках

list1 = [1, 2, 3]
list2 = [1, 4, 3]
 
comparison = [a == b for a, b in zip(list1, list2)]
print(comparison)   # [True, False, True]