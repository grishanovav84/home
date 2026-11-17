import sched
import time
 
s = sched.scheduler(time.time, time.sleep)
 
def my_task():
    print("Эта задача будет отменена.")
 
def cancel_task(event):
    s.cancel(event)
    print("Задача успешно отменена.")
 
event_to_cancel = s.enter(5, 1, my_task)
s.enter(2, 1, cancel_task, (event_to_cancel,))
 
s.run()