import sched
import time
 
s = sched.scheduler(time.time, time.sleep)
 
def repeat_task():
    print(f"[{time.strftime("%H:%M:%S", time.localtime())}] - Hello METANIT.COM")
    # Планируем следующий вызов этой же функции
    s.enter(3, 1, repeat_task)
 
print("Начало повторяющейся задачи...")
s.enter(3, 1, repeat_task)
 
s.run()