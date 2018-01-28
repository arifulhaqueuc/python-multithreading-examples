#!/usr/bin/python

# This is Hello World with Python multithreading.
# A user defined function is created and 
# the function is called when a thread is initialized. 


import threading


def MyFunction():
	"""This is a user defined function"""
	print "Hello World"
	return


def Main():
	t = threading.Thread(target=MyFunction) 	# This is where we create a thread. 
												# Target means run this function 
												# when a thread is initiated.
	t.start() 	# Starting a thread


if __name__ == '__main__':
	Main()
