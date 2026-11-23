
first_name="Tom"
text = f"Hello, {first_name}."
print(text)     # Hello, Tom.
 
name="Bob"
age=23
info = f"Name: {name}\t Age: {age}"
print(info)     # Name: Bob  Age: 23


# Именованные параметры

text = "Hello, {first_name}.".format(first_name="Tom")
print(text)     # Hello, Tom.
 
info = "Name: {name}\t Age: {age}".format(name="Bob", age=23)
print(info)     # Name: Bob  Age: 23


# Параметры по позиции

info = "Name: {0}\t Age: {1}".format("Bob", 23)
print(info)     # Name: Bob  Age: 23

text = "Hello, {0} {0} {0}.".format("Tom")

# Подстановки

welcome = "Hello {:s}"
name = "Tom"
formatted_welcome = welcome.format(name)
print(formatted_welcome)        # Hello Tom

# Форматирование целых чисел

source = "{:d} символов"
number = 5
target = source.format(number)
print(target)   # 5 символов


source = "{:,d} символов"
print(source.format(5000))   # 5,000 символов

# плейсхолдеры можно использовать и в f-строках

n = 5000
source = f"{n:,d} символов"
print(source)   # 5,000 символов

# сколько знаков в дробной части мы хотим вывести

number = 23.8589578
print("{:.2f}".format(number))   # 23.86
print("{:.3f}".format(number))   # 23.859
print("{:.4f}".format(number))   # 23.8590
print("{:,.2f}".format(10001.23554))    # 10,001.24

# установить минимальную ширину форматируемого значения в символах

print("{:10.2f}".format(23.8589578))    #     23.86
print("{:8d}".format(25))               #      25

# Аналогичный пример с f-строками

n1 = 23.8589578
print(f"{n1:10.2f}")    #     23.86
n2 = 25
print(f"{n2:8d}")       #      25

# Для вывода процентов лучше воспользоваться кодом "%"

number = .12345
print("{:%}".format(number))        # 12.345000%
print("{:.0%}".format(number))      # 12%
print("{:.1%}".format(number))      # 12.3%
 
print(f"{number:%}")        # 12.345000%
print(f"{number:.0%}")      # 12%
print(f"{number:.1%}")      # 12.3%

# Для вывода числа в экспоненциальной записи применяется плейсхолдер "e"

number = 12345.6789
print("{:e}".format(number))        # 1.234568e+04
print("{:.0e}".format(number))      # 1e+04
print("{:.1e}".format(number))      # 1.2e+04
 
print(f"{number:e}")        # 1.234568e+04
print(f"{number:.0e}")      # 1e+04
print(f"{number:.1e}")      # 1.2e+04

# Форматирование без метода format

info = "Имя: %s \t Возраст: %d" % ("Tom", 35)
print(info)   # Имя: Tom     Возраст: 35

number = 23.8589578
print("%0.2f  - %e" % (number, number))   # 23.86  - 2.385896e+01

# Установка длины строки

str = "Hello World"
print(f"{str:>16}!")     
print(f"{str:<16}!")   
print(f"{str:^16}!")
print(f"{str:.16}!") 
print(f"{str:.5}!") 