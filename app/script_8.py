## This program creates a thread, 
## officially names it and 
## tries to print the name


#!/usr/bin/python
import threading
import time


def ThreadFunction():
	print threading.currentThread().getName(), "Starting"
	time.sleep(2)
	print threading.currentThread().getName(), "Exiting"

def ServiceFunction():
	print threading.currentThread().getName(), "Starting"
	time.sleep(3)
	print threading.currentThread().getName(), "Exiting"


def Main():
	myThread = threading.Thread(
		name='Service Function', 
		target=ServiceFunction
	)
	w = threading.Thread(
		name='Thread function',
		target=ThreadFunction
	)
	w2 = threading.Thread(
		target=ThreadFunction
	)

	w.start()
	w2.start()
	myThread.start()


if __name__ == "__main__":
	Main()

