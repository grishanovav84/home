import sched
import time
 
s = sched.scheduler(time.time, time.sleep)
 
def repeat_task():
    print(f"[{time.strftime("%H:%M:%S", time.localtime())}] - Hello METANIT.COM")
 
print("Начало повторяющейся задачи...")
 
count = 5   # 5 раз выполняем задачу
 
while count:
    s.enter(3, 1, repeat_task)
    s.run()
    count -= 1