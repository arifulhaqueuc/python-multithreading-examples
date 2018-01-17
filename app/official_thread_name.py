# Write a program which creates a thread, officially names it and tries to print the name

import threading
import time

def uf():
	print threading.currentThread().getName(), "Starting"
	time.sleep(2)
	print threading.currentThread().getName(), "Exiting"

def service_function():
	print threading.currentThread().getName(), "Starting"
	time.sleep(3)
	print threading.currentThread().getName(), "Exiting"

t = threading.Thread(name='service_function', 
	target=service_function)	
w = threading.Thread(name='uf',
	target=uf)
w2 = threading.Thread(target=uf)

w.start()
w2.start()
t.start()
