# This program creates five threads which in turn each will print "Hello World" on the screen

import threading

def uf():
	"""User defined Thread function"""
	print "Hello World"
	return


## 1st apprach to get the for loop running
if __name__ == "__main__":
	threads = [] # Threads list needed when we use a bulk of threads
	for i in range(5):
		t = threading.Thread(target=uf)
		threads.append(t)
		t.start()


## 2nd approach would be as follows
"""
threads = []
for i in range(5):
	t = threading.Thread(target=uf)
	threads.append(t)
	t.start()
"""
