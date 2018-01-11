"""This is a simple program to print Hello World using threading. A user defined function is created and the function is called when a thread has been initialized. 
"""

import threading


def uf():
 """This is a user defined function"""
 print "Hello World"
 return

# This is a thread list
#threads = []
t = threading.Thread(target=uf) # Creating a thread
# Target means run this function when a thread has been initiated
#threads.append(t)
t.start() # Starting a thread

