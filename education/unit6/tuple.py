# Кортеж (tuple) представляет последовательность элементов, которая во многом похожа на список за тем исключением, что кортеж является неизменяемым (immutable) типом

tom = ("Tom", 23)
print(tom)     # ("Tom", 23)

tom = "Tom", 23
print(tom)     # ("Tom", 23)


tom = ("Tom",)

# создание кортежа из другого набора элементов

data = ["Tom", 37, "Google"]
tom = tuple(data)
print(tom)      # ("Tom", 37, "Google")


# Обращение к элементам кортежа

tom = ("Tom", 37, "Google", "software developer")
print(tom[0])       # Tom
print(tom[1])       # 37
print(tom[-1])      # software developer

name, age, company, position = ("Tom", 37, "Google", "software developer")
print(name)         # Tom
print(age)          # 37
print(position)     # software developer
print(company)     # Google


# Получение подкортежей

tom = ("Tom", 37, "Google", "software developer")
 
# получем подкортеж с 1 по 3 элемента (не включая)
print(tom[1:3])     # (37, "Google")
 
# получем подкортеж с 0 по 3 элемента (не включая)
print(tom[:3])     # ("Tom", 37, "Google")
 
# получем подкортеж с 1 по послдений элемент
print(tom[1:])     # (37, "Google", "software developer")

# Кортеж как параметр и результат функций

def get_user():
    name = "Tom"
    age = 22
    company = "Google"
    return name, age, company
 
 
user = get_user()
print(user)     # ("Tom", 37, "Google")


# При передаче кортежа в функцию с помощью оператора * его можно разложить на отдельные значения

def print_person(name, age, company):
    print(f"Name: {name}  Age: {age}  Company: {company}")
 
tom = ("Tom", 22)
print_person(*tom, "Microsoft")     # Name: Tom  Age: 22  Company: Microsoft
 
bob = ("Bob", 41, "Apple")
print_person(*bob)      # Name: Bob  Age: 41  Company: Apple

# Перебор кортежей
tom = ("Tom", 22, "Google")
for item in tom:
    print(item)


tom = ("Tom", 22, "Google")
 
i = 0
while i < len(tom):
    print(tom[i])
    i += 1

# Проверка наличия значения

user = ("Tom", 22, "Google")
name = "Tom"
if name in user:
    print("Пользователя зовут Tom")
else:
    print("Пользователь имеет другое имя")