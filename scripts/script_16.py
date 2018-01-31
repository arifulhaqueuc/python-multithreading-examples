## This function returns a list of all active threads. 

import threading
for thread in threading.enumerate():
    print("Thread name is %s." % thread.getName())
    
