#!/usr/bin/python

import threading
import time


## This multithreading program runs five times
## and each time the program takes two numbers as given input
## and print sum of them.


def MyThread(num1, num2):
	print "Given Numbers: %s, %s" %(num1, num2)
	sum1= int(num1) + int(num2)
	print "Result: %d" %sum1
	return


def Main():
	threads = []
	for i in range(5):
		t = threading.Thread(target=MyThread, args=(10,20))
		threads.append(t)
		time.sleep(0.5)
		t.start()


if __name__ == '__main__':
	Main()
	