# This multithreading program creates five threads 
# and each thread prints "Hello World" with a two-second interval


#!/usr/bin/python
import threading
import time


def HelloWorld():
	"""User defined Thread function"""
	print "Hello World"
	return


def Main():
	threads = [] # Threads list needed when we use a bulk of threads
	print "Program started.  This program will print Hello World five times..."
	for i in range(5):
		mythread = threading.Thread(target=HelloWorld)
		threads.append(mythread)
		time.sleep(2)
		mythread.start()
	print "Done! Program ended"


if __name__ == "__main__":
	Main()
