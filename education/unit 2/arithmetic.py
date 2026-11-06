number = 3 + 4 * 5 ** 2 + 7
print(number)  # 110

number = (3 + 4) * (5 ** 2 + 7)
print(number)  # 224

number = 10
number += 5
print(number)  # 15
 
number -= 3
print(number)  # 12
 
number *= 4
print(number)  # 48

first_number = 2.0001
second_number = 5
third_number = first_number / second_number
print(third_number) # 0.40002000000000004

first_number = 2.0001
second_number = 0.1
third_number = first_number + second_number
print(round(third_number))  # 2

first_number = 2.0001
second_number = 0.1
third_number = first_number + second_number
print(round(third_number, 4))  # 2.1001

# округление до целого числа
print(round(2.49))  # 2 - округление до ближайшего целого 2
print(round(2.51))  # 3

print(round(2.5))   # 2 - ближайшее четное
print(round(3.5))   # 4 - ближайшее четное

# округление до двух знаков после запятой
print(round(2.554, 2))      # 2.55
print(round(2.5551, 2))      # 2.56
print(round(2.554999, 2))   # 2.55
print(round(2.499, 2))      # 2.5


# округление до двух знаков после запятой
print(round(2.545, 2))   # 2.54
print(round(2.555, 2))   # 2.56 - округление до четного
print(round(2.565, 2))   # 2.56
print(round(2.575, 2))   # 2.58
 
print(round(2.655, 2))   # 2.65 - округление не до четного
print(round(2.665, 2))   # 2.67
print(round(2.675, 2))   # 2.67