
import time
from threading import Thread

#create function for thread
def Tfunc(i):
 print("%d sleeping 5 sec from thread\n" % i)
 time.sleep(5)
 print("\n %d finished sleeping from thread" % i)

#start the thread for function
for i in range(5):
 t1 = Thread(target=Tfunc, args=(i,))
 t1.start()
 
 
