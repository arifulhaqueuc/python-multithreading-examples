"""Write a program that adds two numbers and prints the result"""

import threading 

def uf(num1, num2):
	"""This is user defined thread function"""
	print "Given numbers= %s, %s" %(num1, num2)
	print "Result = %d" %(int(num1)+int(num2))
	return


if __name__ == '__main__':
	t = threading.Thread(target=uf, args=(2,3))
	t.start()
