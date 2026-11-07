sum = lambda a, b: a + b
 
print(sum(4, 5))    # 9
print(sum(5, 6))    # 11


def do_operation(a, b, operation):
    result = operation(a, b)
    print(f"result = {result}")
 
do_operation(5, 4, lambda a, b: a + b)  # result = 9
do_operation(5, 4, lambda a, b: a * b)  # result = 20


def select_operation2(choice):
    if choice == 1:
        return lambda a, b: a + b
    elif choice == 2:
        return lambda a, b: a - b
    else:
        return lambda a, b: a * b
 
 
operation = select_operation2(1)  # operation = sum
print(operation(10, 6))  # 16
 
operation = select_operation2(2)  # operation = subtract
print(operation(10, 6))  # 4
 
operation = select_operation2(3)  # operation = multiply
print(operation(10, 6))  # 60

