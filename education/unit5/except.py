try:
    number = int(input("Введите число: "))
    print("Введенное число:", number)
except:
    print("Преобразование прошло неудачно")
finally:
    print("Блок try завершил выполнение")
print("Завершение программы")


try:
    number = 3/0    # генерирует исключение ZeroDivisionError
    print(number)
finally:
    print("Блок try завершил выполнение")
print("Завершение программы")