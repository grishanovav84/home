import timeit 
 
def sum():
    result = 0
    for n in range(100): 
        result += n
    return result
 
start = timeit.default_timer()
print("Start time:", start)
sum()
print("Execution time:", timeit.default_timer() - start)