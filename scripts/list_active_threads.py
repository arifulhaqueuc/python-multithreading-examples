#!/usr/bin/python


## This function returns a list of all active threads. 


import threading


def Main():
	for thread in threading.enumerate():
	    print("Thread name is %s." % thread.getName())
	    

if __name__ == '__main__':
	Main()
