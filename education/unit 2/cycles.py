number = 1
 
while number < 5:
    print(f"number = {number}")
    number += 1
print("Работа программы завершена")



number = 1
 
while number < 5:
    print(f"number = {number}")
    number += 1
else:
    print(f"number = {number}. Работа цикла завершена")
print("Работа программы завершена")


number = 10
 
while number < 5:
    print(f"number = {number}")
    number += 1
else:
    print(f"number = {number}. Работа цикла завершена")
print("Работа программы завершена")



message = "Hello"
 
for c in message:
    print(c)


for n in range(10):
    print(n, end=" ")    


for n in range(4, 10):
    print(n, end=" ")   


for n in range(0, 10, 2):
    print(n, end=" ")


message = "Hello"
for c in message:
    print(c)
else:
    print(f"Последний символ: {c}. Цикл завершен");
print("Работа программы завершена")  # инструкция не имеет отступа, поэтому не относится к else



#


i = 1
j = 1
while i < 10:
    while j < 10:
        print(i * j, end="\t")
        j += 1
    print("\n")
    j = 1
    i += 1



for c1 in  "ab":
    for c2 in "ba":
        print(f"{c1}{c2}")



number = 0
while number < 5:
    number += 1
    if number == 3 :    # если number = 3, выходим из цикла
        break
    print(f"number = {number}")



number = 0
while number < 5:
    number += 1
    if number == 3 :    # если number = 3, переходим к новой итерации цикла
        continue
    print(f"number = {number}")