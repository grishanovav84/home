# определение функции декоратора
def select(input_func):    
    def output_func():      # определяем функцию, которая будет выполняться вместо оригинальной
        print("*****************")  # перед выводом оригинальной функции выводим всякую звездочки
        input_func()                # вызов оригинальной функции
        print("*****************")  # после вывода оригинальной функции выводим всякую звездочки
    return output_func     # возвращаем новую функцию
 
# определение оригинальной функции
@select         # применение декоратора select
def hello():
    print("Hello")
 
# вызов оригинальной функции
hello()




# определение функции декоратора
def check(input_func):    
    def output_func(*args):      # через *args получаем значения параметров оригинальной функции
        input_func(*args)                # вызов оригинальной функции
    return output_func     # возвращаем новую функцию
 
# определение оригинальной функции
@check
def print_person(name, age):
    print(f"Name: {name}  Age: {age}")
 
# вызов оригинальной функции
print_person("Tom", 38)




# определение функции декоратора
def check2(input_func):    
    def output_func(*args):
        name = args[0]
        age = args[1]           # получаем значение второго параметра
        if age < 0: age = 1     # если возраст отрицательный, изменяем его значение на 1
        input_func(name, age)   # передаем функции значения для параметров
    return output_func
 
# определение оригинальной функции
@check2
def print_person2(name, age):
    print(f"Name: {name}  Age: {age}")
 
# вызов оригинальной функции
print_person2("Tom", 38)
print_person2("Bob", -5)