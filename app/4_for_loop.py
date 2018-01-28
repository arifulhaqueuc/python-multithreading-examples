#!/usr/bin/python


# This multithreading program creates five threads 
# and each thread prints "Hello World" with a two-second interval


import threading
import time


def HelloWorld():
	"""User defined Thread function"""
	print "Hello World"
	return


def Main():
	threads = [] # Threads list needed when we use a bulk of threads
	print "Program started"
	for i in range(5):
		t = threading.Thread(target=HelloWorld)
		threads.append(t)
		time.sleep(2)
		t.start()
	print "Program ended"


## 1st apprach to get the for loop running
if __name__ == "__main__":
	Main()
