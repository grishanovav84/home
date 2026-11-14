try:
    age = int(input("Введите возраст: "))
    if age > 110 or age < 1:
        raise Exception("Некорректный возраст")
    print("Ваш возраст:", age)
except ValueError:
    print("Введены некорректные данные")
except Exception as e:
    print(e)
print("Завершение программы")