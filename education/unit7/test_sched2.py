import sched
import time
 
s = sched.scheduler(time.time, time.sleep)
 
def print_message(message):
    print(f"[{time.strftime("%H:%M:%S", time.localtime())}] - {message}")
 
print("Начало планирования...")
 
s.enter(3, 1, print_message, ("Первое сообщение (через 3 секунды)",))
s.enter(5, 1, print_message, ("Второе сообщение (через 5 секунд)",))
s.enter(5, 2, print_message, ("Третье сообщение (через 5 секунд, но с более низким приоритетом)",))
 
# Событие с приоритетом 1 будет выполнено раньше, чем событие с приоритетом 2, если время совпадает.
 
s.run()
print("Планирование завершено.")