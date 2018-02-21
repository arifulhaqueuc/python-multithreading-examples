

import threading
import time 
# global variable x
x = 0
 
def Tfunc(i,lock):
 lock.acquire()
 print('from thread %d' %i)
 lock.release()
 
 
 # creating a lock
lock = threading.Lock()
 
 # creating threads
t1 = threading.Thread(target=Tfunc, args=(1,lock,))
t2 = threading.Thread(target=Tfunc, args=(2,lock,))
 
 # start threads
t1.start()
t2.start()
 
 # wait until threads finish their job
t1.join()
time.sleep(5)
t2.join()

