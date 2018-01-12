## This program creates five threads which in turn each will print "Hello World" on the screen

import threading

def uf():
	"""User defined Thread function"""
	print "Hello World"
	return

if __name__ == "__main__":
	threads = [] # Threads list needed when we use a bulk of threads
	for i in range(5):
		t = threading.Thread(target=uf)
		threads.append(t)
		t.start()
