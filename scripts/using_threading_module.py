

import time
import threading 

#create function for thread
def Tfunc(i):
 print("Thread no.:%d" % (i+1))
 time.sleep(5)
 print("%d finished sleeping from thread\n" % i)

#start the thread for function
for i in range(3):
 t1 = threading.Thread(target=Tfunc, args=(i,))
 t1.start()
 
#check thread is alive or not
 c=t1.isAlive()

#fetch the name of thread
 c1=t1.getName()
 print('\n',c1,"is Alive:",c)

#get toatal number of thread in execution
 count=threading.active_count()
 print("Total No of threads:",count)
 
 
