def say_hello():    # определение функции say_hello
    print("Hello")
 
 
say_hello()         # вызов функции say_hello


def say_hello2(): print("Hello2")
 
say_hello2()


def say_hello3():
    print("Hello3")
 
 
def say_goodbye():
    print("Good Bye")
 
 
say_hello3()
say_goodbye()


def print_messages():
    # определение локальных функций
    def say_hello(): print("print Hello")
    def say_goodbye(): print("print Good Bye")
    # вызов локальных функций
    say_hello()
    say_goodbye()
 
# Вызов функции print_messages
print_messages()




def main():
    say_hello4()
    say_goodbye4()
 
def say_hello4():
    print("Hello4")
 
def say_goodbye4():
    print("Good Bye4")
 
# Вызов функции main
main()