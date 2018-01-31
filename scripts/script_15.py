## This function of threading module is used to create a new Thread and letting it know that it should only start after a specified time. 
## Once it starts, it should call the specified function.

import threading

def delayed():
    print("I am printed after 5 seconds!")

thread = threading.Timer(3, delayed)
thr
