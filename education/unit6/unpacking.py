
x, y = (1, 2)
print(x)    # 1
print(y)    # 2


name, age, company = ("Tom", 38, "Google")
print(name)         # Tom
print(age)          # 38
print(company)      # Google

people = ["Tom", "Bob", "Sam"]
first, second, third = people
print(first)      # Tom
print(second)     # Bob
print(third)      # Sam


dictionary = {"red": "красный", "blue": "синий", "green": "зеленый"}
r, b, g = dictionary
print(r)    # red
print(b)    # blue
print(g)    # green
# получаем значение по ключу
print(dictionary[g])    # зеленый



# Деструктуризация в циклах


people = [
    ("Tom", 38, "Google"),
    ("Bob", 42, "Microsoft"),
    ("Sam", 29, "JetBrains")
]
 
for name, age, company in people:
    print(f"Name: {name}, Age: {age}, Company: {company}")


people2 = ["Tom", "Bob", "Sam"]
for index, name in enumerate(people2):
    print(f"{index}.{name}")
 
# результат
# 0.Tom
# 1.Bob
# 2.Sam



# Игнорирование значений

person =("Tom", 38, "Google")
name, _, company = person
print(name)     # Tom
print(company)  # Google

# Упаковка значений и оператор *

num1=1
num2=2
num3=3
*numbers,=num1,num2,num3
print(numbers)  #[1, 2, 3]


# упаковка применяется для сбора значений, которые остались после присвоения результатов деструктуризации
head, *tail = [1, 2, 3, 4, 5]
 
print(head)  # 1
print(tail)  # [2, 3, 4, 5]


# получить все кроме последнего

*head, tail = [1, 2, 3, 4, 5]
 
print(head)  # [1, 2, 3, 4]
print(tail)  # 5

# элементы по середине, кроме первого и последнего

head, *middle, tail = [1, 2, 3, 4, 5]
 
print(head)    # 1
print(middle)  # [2, 3, 4]
print(tail)    # 5

# все кроме первого и второго

first, second, *other = [1, 2, 3, 4, 5]
 
print(first)    # 1
print(second)   # 2
print(other)    # [3, 4, 5]

# Распаковка и операторы * и **

nums1 = [1, 2, 3]
nums2 = (4, 5, 6)
 
# распаковываем список nums1 и кортеж nums2
nums3 = [*nums1, *nums2] 
print(nums3)        # [1, 2, 3, 4, 5, 6]


dictionary1 = {"red":"красный", "blue":"синий"}
dictionary2 = {"green":"зеленый", "yellow":"желтый"}
 
# распаковываем словари
dictionary3 = {**dictionary1, **dictionary2}
print(dictionary3)  # {'red': 'красный', 'blue': 'синий', 'green': 'зеленый', 'yellow': 'желтый'}


