import sched
import time
 
def print_message():
    print("Hello METANIT.COM!")
 
# создаем scheduler
s = sched.scheduler(time.time, time.sleep)
print("Начало планирования...")
 
# планируем выполнение через 3 минуты
s.enter(3, 1, print_message)
 
# запускаем выполнение
s.run()
 
print("Планирование завершено.")