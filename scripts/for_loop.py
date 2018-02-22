import time
from threading import Thread


def ThreadFunction(x):
    print "sleeping 5 sec from thread %d" % x
    time.sleep(5)
    print "finished sleeping from thread %d" % x

def Main():
  for i in range(10):
      myThread = Thread(target=ThreadFunction, args=(i,))
      myThread.start()
      
if __name__ == "__main__":
  Main()
  
