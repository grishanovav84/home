a = 2       # число int
b = 2.5     # число float
c = a + b
print(c)    # 4.5

#a = "2"
#b = 3
#c = a + b

a = "2"
b = 3
c = int(a) + b
print(c)    # 5


a = int(15)     # a = 15
b = int(3.7)    # b = 3
c = int("4")    # c = 4
e = int(False)    # e = 0
f = int(True)     # f = 1



a = "2.7"
b = 3
c = float(a) + b
print(c) # 5.7


a = str(False)      # a = "False"
b = str(True)       # b = "True"
c = str(5)         # c = "5"
d = str(5.7)       # d = "5.7"


#age = 22
#message = "Age: " + age     # Ошибка
#print(message)


age = 22
message = "Age: " + str(age)   # Age: 22
print(message)