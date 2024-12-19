import time 
import threading

def taks_1(task_number):
    print(f"task {task_number}  ongoing....")
    time.sleep(5)
    

for i in range(10000):
    t1 = threading.Thread(target=taks_1,args=[i])
    t1.start()


