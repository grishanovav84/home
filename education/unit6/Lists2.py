
people = ["Tom", "Sam", "Bob"]

# получение элементов с начала списка
print(people[0])   # Tom
print(people[1])   # Sam
print(people[2])   # Bob
 
# получение элементов с конца списка
print(people[-2])   # Sam
print(people[-1])   # Bob
print(people[-3])   # Tom


people2 = ["Tom", "Sam", "Bob"]
 
people2[1] = "Mike"  # изменение второго элемента
print(people2[1])    # Mike
print(people2)       # ["Tom", "Mike", "Bob"]

# python позволяет разложить список
people3 = ["Tom", "Bob", "Sam"]
 
tom, bob, sam = people3
 
print(tom)      # Tom
print(bob)      # Bob
print(sam)      # Sam

# Перебор элементов
people4 = ["Tom1", "Sam1", "Bob1"]
for person in people4:
    print(person)


people5 = ["Tom2", "Sam2", "Bob2"]
i = 0
while i < len(people5):
    print(people5[i])    # применяем индекс для получения элемента
    i += 1

# Сравнение списков

numbers1 = [1, 2, 3, 4, 5]
numbers2 = list([1, 2, 3, 4, 5])
if numbers1 == numbers2:
    print("numbers1 equal to numbers2")
else:
    print("numbers1 is not equal to numbers2")


# Получение части списка   

people6 = ["Tom", "Bob", "Alice", "Sam", "Tim", "Bill"]
 
slice_people1 = people6[:3]   # с 0 по 3
print(slice_people1)   # ["Tom", "Bob", "Alice"]
 
slice_people2 = people6[1:3]   # с 1 по 3
print(slice_people2)   # ["Bob", "Alice"]
 
slice_people3 = people6[1:6:2]   # с 1 по 6 с шагом 2
print(slice_people3)   # ["Bob", "Sam", "Bill"]


# можно использовать отрицательные индексы, тогда отсчет будет идти с конца
people7 = ["Tom", "Bob", "Alice", "Sam", "Tim", "Bill"]
 
slice_people1 = people7[:-1]   # с предпоследнего по нулевой
print(slice_people1)   # ["Tom", "Bob", "Alice", "Sam", "Tim"]
 
slice_people2 = people7[-3:-1]   # с третьего с конца по предпоследний
print(slice_people2)   # [ "Sam", "Tim"]