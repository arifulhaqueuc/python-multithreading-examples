# This multithreading program outputs default thread name when 
# the thread is being executed.


#!/usr/bin/python
import threading
import time


def ThreadFunction():
	print threading.currentThread().getName(), "Starting"
	time.sleep(2)
	print threading.currentThread().getName(), "Exiting"


def Main():
	w = threading.Thread(target=ThreadFunction)
	w.start()


if __name__ == '__main__':
	Main()