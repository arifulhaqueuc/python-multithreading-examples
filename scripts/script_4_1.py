## This program prints 1 to 10 with threading module


#!/usr/bin/python
import threading
import time


def PrintNumber():
    for i in range(1, 11):
        time.sleep(1)
        print(i)


def Main():
	print "Program started.  This program will print number 1 to 10..."
	mythread = threading.Thread(target=PrintNumber)
	mythread.start()


if __name__ == "__main__":
	Main()
