
# начинается или оканчивается строка на определенную подстроку
file_name = "hello.py"
 
starts_with_hello = file_name.startswith("hello")   # True
ends_with_exe = file_name.endswith("exe")           # False

# Удаление пробелов в начале и в конце строки
string = "   hello  world!  "
string = string.strip()
print(string)           # hello  world!


# Дополнение строки пробелами и выравнивание

print("iPhone 7:", "52000".rjust(10))
print("Huawei P10:", "36000".rjust(10))

# Поиск в строке
welcome = "Hello world! Goodbye world!"
index = welcome.find("wor")
print(index)       # 6
 
# поиск с 10-го индекса
index = welcome.find("wor",10)
print(index)       # 21
 
# поиск с 10 по 15 индекс
index = welcome.find("wor",10,15)
print(index)       # -1


# Замена в строке

phone = "+1-234-567-89-10"
 
# замена дефисов на пробел
edited_phone = phone.replace("-", " ")
print(edited_phone)     # +1 234 567 89 10
 
# удаление дефисов
edited_phone = phone.replace("-", "")
print(edited_phone)     # +12345678910
 
# замена только первого дефиса
edited_phone = phone.replace("-", "", 1)
print(edited_phone)     # +1234-567-89-10


# Разделение на подстроки

text = "Это был огромный, в два обхвата дуб, с обломанными ветвями и с обломанной корой"
# разделение по пробелам
splitted_text = text.split()
print(splitted_text)
print(splitted_text[6])     # дуб,
 
# разбиение по запятым
splitted_text = text.split(",")
print(splitted_text)
print(splitted_text[1])     # в два обхвата дуб
 
# разбиение по первым пяти пробелам
splitted_text = text.split(" ", 5)
print(splitted_text)        
print(splitted_text[5])     # обхвата дуб, с обломанными ветвями и с обломанной корой

# Еще один метод - partition() разбивает строку по разделителю
text = "Это был огромный, в два обхвата дуб, с обломанными ветвями и с обломанной корой"
text_parts = text.partition("дуб")
print(text_parts)


# Соединение строк

words = ["Let", "me", "speak", "from", "my", "heart", "in", "English"]
 
# разделитель - пробел
sentence = " ".join(words)
print(sentence)  # Let me speak from my heart in English
 
# разделитель - вертикальная черта
sentence = " | ".join(words)
print(sentence)  # Let | me | speak | from | my | heart | in | English

word = "hello"
joined_word = "|".join(word)
print(joined_word)      # h|e|l|l|o
