
# хранит коллекцию элементов, где каждый элемент имеет уникальный ключ

users = {1: "Tom", 2: "Bob", 3: "Bill"}
print(users)

emails = {"tom@gmail.com": "Tom", "bob@gmai.com": "Bob", "sam@gmail.com": "Sam"}
print(emails)

objects = {1: "Tom", "2": True, 3: 100.6}

print(objects)

objects = {}
objects = dict()


# Преобразование списков и кортежей в словарь

users_list = [
    ["+111123455", "Tom"],
    ["+384767557", "Bob"],
    ["+958758767", "Alice"]
]
users_dict = dict(users_list)
print(users_dict)      # {"+111123455": "Tom", "+384767557": "Bob", "+958758767": "Alice"}


users_tuple = (
    ("+111123455", "Tom"),
    ("+384767557", "Bob"),
    ("+958758767", "Alice")
)
users_dict = dict(users_tuple)
print(users_dict)


# Получение и изменение элементов
users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
 
# получаем элемент с ключом "+11111111"
print(users["+11111111"])      # Tom
 
# установка значения элемента с ключом "+33333333"
users["+33333333"] = "Bob Smith"
print(users["+33333333"])   # Bob Smith


key = "+4444444"
if key in users:
    user = users[key]
    print(user)
else:
    print("Элемент не найден")



users2 = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
 
user1 = users2.get("+55555555")
print(user1)    # Alice
user2 = users2.get("+33333333", "Unknown user")
print(user2)    # Bob
user3 = users2.get("+44444444", "Unknown user")
print(user3)    # Unknown user



# Удаление

users3 = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
 
del users3["+55555555"]
print(users3)    # { "+11111111": "Tom", "+33333333": "Bob"}


users4 = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
 
key = "+55555555"
if key in users4:
    del users4[key]
    print(f"Элемент с ключом {key} удален")
else:
    print("Элемент не найден")



users5 = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
key = "+55555555"
user = users5.pop(key)
print(user)     # Alice
 
user = users5.pop("+4444444", "Unknown user")
print(user)     # Unknown user

# необходимо удалить все элементы
users.clear()

print('after clear')
print(users)


# Копирование и объединение словарей
users0 = {"+1111111": "Tom", "+3333333": "Bob", "+5555555": "Alice"}
students = users0.copy()
print(students)     # {"+1111111": "Tom", "+3333333": "Bob", "+5555555": "Alice"}

users1 = {"+1111111": "Tom", "+3333333": "Bob"}
 
users2 = {"+2222222": "Sam", "+6666666": "Kate"}
users1.update(users2)
 
print(users1)    # {"+1111111": "Tom", "+3333333": "Bob", "+2222222": "Sam", "+6666666": "Kate"}
print(users2)   # {"+2222222": "Sam", "+6666666": "Kate"}


# Перебор словаря

users5 = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
for key in users5:
    print(f"Phone: {key}  User: {users5[key]} ")


users6 = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
for key, value in users6.items():
    print(f"Phone: {key}  User: {value} ")    


# перебор ключей
for key in users6.keys():
    print(key)

# перебор значений
for value in users6.values():
    print(value)