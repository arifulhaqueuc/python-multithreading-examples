## This function returns the number of threads currently in execution. 
## Let us modify the last script’s ThreadFunction function.

import time
import threading
from threading import Thread

def ThreadFunction(i):
    print("Thread %i going to sleep for 5 seconds." % i)
    time.sleep(5)
    print("Thread %i is awake now." % i)

def Main():
  for i in range(10):
      myThread = Thread(target=ThreadFunction, args=(i, ))
      myThread.start()
      print("Current Thread count: %i." % threading.active_count())
    
    
if __name__ == "__main__":    
  Main()
  
