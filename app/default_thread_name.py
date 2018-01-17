# Write a program that outputs default thread name when thread is being executed.

import threading
import time

def uf():
	print threading.currentThread().getName(), "Starting"
	time.sleep(2)
	print threading.currentThread().getName(), "Exiting"


w = threading.Thread(target=uf) ## using default name
w.start()