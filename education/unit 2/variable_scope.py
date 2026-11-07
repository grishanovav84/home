name = "Tom"
 
 
def say_hi():
    print("Hello", name)
 
 
def say_bye():
    print("Good bye", name)
 
say_hi()
say_bye()



def say_hi2():
    name = "Sam"
    surname = "Johnson"
    print("Hello", name, surname)
 
 
def say_bye2():
    name = "Tom"
    print("Good bye", name)
 
say_hi2()
say_bye2()



name = "Tom"
 
 
def say_hi3():
    name = "Bob"        # скрываем значение глобальной переменной
    print("Hello", name)
 
 
def say_bye3():
    print("Good bye", name)
 
 
say_hi3()    # Hello Bob
say_bye3()   # Good bye Tom





name = "Tom"
 
 
def say_hi5():
    global  name
    name = "Bob"        # изменяем значение глобальной переменной
    print("Hello", name)
 
 
def say_bye5():
    print("Good bye", name)
 
 
say_hi5()    # Hello Bob
say_bye5()   # Good bye Bob



#nonlocal
def outer():  # внешняя функция
    n = 5
 
    def inner():    # вложенная функция
        print(n)
 
    inner()     # 5
    print(n)
 
 
outer()     # 5





def outer2():  # внешняя функция
    n = 5
 
    def inner():    # вложенная функция
        n = 25
        print(n)
 
    inner()     # 25
    print(n)
 
 
outer2()     # 5 
# 25    - inner
# 5     - outer




def outer3():  # внешняя функция
    n = 5
 
    def inner():    # вложенная функция
        nonlocal n  # указываем, что n - это переменная из окружающей функции
        n = 25
        print(n)
 
    inner()     # 25
    print(n)
 
 
outer3()          # 25