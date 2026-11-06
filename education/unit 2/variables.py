name = "Tom"  # переменной name равна "Tom"
print(name)   # выводит: Tom
name = "Bob"  # меняем значение на "Bob"
print(name)   # выводит: Bob

isMarried = False
print(isMarried)    # False
 
isAlive = True
print(isAlive)      # True

age = 21
print("Возраст:", age)    # Возраст: 21
 
count = 15
print("Количество:", count) # Количество: 15


height = 1.68
pi = 3.14
weight = 68.
print(height)   # 1.68
print(pi)       # 3.14
print(weight)   # 68.0


x = 3.9e3
print(x)  # 3900.0
 
x = 3.9e-3
print(x)  # 0.0039


message = "Hello World!"
print(message)  # Hello World!
 
name = 'Tom'
print(name)  # Tom


text = ("Laudate omnes gentes laudate "
        "Magnificat in secula ")
print(text)


'''
Это комментарий
'''
text = '''Laudate omnes gentes laudate
Magnificat in secula
Et anima mea laudate
Magnificat in secula 
'''
print(text)


text = "Message:\n\"Hello World\""
print(text)

path = "C:\python\name.txt"
print(path)


userName = "Tom"
userAge = 37
user = f"name: {userName}  age: {userAge}"
print(user)   # name: Tom  age: 37


userId = "abc"  # тип str
print(userId)
 
userId = 234  # тип int
print(userId)


userId = "abc"      # тип str
print(type(userId)) # <class 'str'>
 
userId = 234        # тип int
print(type(userId)) # <class 'int'>