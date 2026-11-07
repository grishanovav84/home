def say_hello(): print("Hello")
def say_goodbye(): print("Good Bye")
 
message = say_hello
message()       # Hello
message = say_goodbye
message()       # Good Bye


def sum(a, b): return a + b
def multiply(a, b): return a * b
 
operation = sum
result = operation(5, 6)
print(result)   # 11
 
operation = multiply
print(operation(5, 6))      # 30


def do_operation(a, b, operation):
    result = operation(a, b)
    print(f"result = {result}")
 
def sum2(a, b): return a + b
def multiply(a, b): return a * b
 
do_operation(5, 4, sum2)         # result = 9
do_operation(5, 4, multiply)   # result = 20