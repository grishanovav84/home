
message = "Hello World!"
print(message)  # Hello World!
 
name = 'Tom'
print(name)  # Tom


text = ("Laudate omnes gentes laudate "
        "Magnificat in secula ")
print(text)

# Вставка значений в строку

userName = "Tom"
userAge = 37
user = f"name: {userName}  age: {userAge}"
print(user)   # name: Tom  age: 37


# Обращение к символам строки

string = "hello world"
c0 = string[0]  # h
print(c0)
c6 = string[6]  # w
print(c6)
 
# c11 = string[11]  # ошибка IndexError: string index out of range
# print(c11)

# Перебор строки
string = "hello world"
for char in string:
    print(char)

# Используем все варианты получения подстроки
string = "hello world"
 
# с 0 до 5 индекса
sub_string1 = string[:5]
print(sub_string1)      # hello
 
# со 2 до 5 индекса
sub_string2 = string[2:5]
print(sub_string2)      # llo
 
# с 2 по 9 индекса через один символ
sub_string3 = string[2:9:2]
print(sub_string3)      # lowr    


# Объединение строк

name = "Tom"
surname = "Smith"
fullname = name + " " + surname
print(fullname)  # Tom Smith


name = "Tom"
age = 33
info = "Name: " + name + " Age: " + str(age)
print(info)  # Name: Tom Age: 33


name = "Tom"
age = 33
info = "Name: " + name + " Age: " + str(age)
print(info)  # Name: Tom Age: 33


# Сравнение строк


str1 = "1a"
str2 = "aa"
str3 = "Aa"
print(str1 > str2)  # False, так как первый символ в str1 - цифра
print(str2 > str3)  # True, так как первый символ в str2 - в нижнем регистре


str1 = "Tom"
str2 = "tom"
print(str1 == str2)  # False - строки не равны
 
print(str1.lower() == str2.lower())  # True

# Функции ord и len
	
print(ord("A"))     # 65

string = "hello world"
length = len(string)
print(length)   # 11


# Поиск в строке

text = "hello world"
exist = "hello" in text
print(exist)    # True
 
exist = "sword" in text
print(exist)    # False


text = "hello world"
print("hello" not in text)    # False
print("sword" not in text)    # True