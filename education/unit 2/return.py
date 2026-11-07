
def sum(a, b):
    return a + b
 
 
result = sum(4, 6)                  # result = 0
print(f"sum(4, 6) = {result}")      # sum(4, 6) = 10
print(f"sum(3, 5) = {sum(3, 5)}")   # sum(3, 5) = 8


def get_message():
    return "Hello METANIT.COM"
    print("End of the function")
 
print(get_message())



def print_person2(name, age):
    if age > 120 or age < 1:
        print("Invalid age")
        return
    print(f"Name: {name}  Age: {age}")
 
 
print_person2("Tom", 22)
print_person2("Bob", -102)