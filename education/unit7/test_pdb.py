import pdb
 
def sum(a, b):
    pdb.set_trace() # <--- Программа остановится здесь
    result = a + b
    return result
 
# print(sum(5, 6))




def total(numbers):
    s = 0
    for n in numbers:
        s = s + n
        breakpoint()
    return s
 
print(total([1, "2", 3, 4]))

