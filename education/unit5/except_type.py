class Person:
    def __init__(self, name, age):
        self.__name = name  # устанавливаем имя
        self.__age = age   # устанавливаем возраст
 
    def display_info(self):
        print(f"Имя: {self.__name}  Возраст: {self.__age}")




        