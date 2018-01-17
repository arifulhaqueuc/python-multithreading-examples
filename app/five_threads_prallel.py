# 

import threading

def uf(num1, num2):
	"""Thread uf function"""
	print "Number: %s %s" %(num1, num2)
	sum1= int(num1) + int(num2)
	print "Result: %d" %sum1
	return


threads = []
for i in range(5):
	t = threading.Thread(target=uf, args=(10,20))
	threads.append(t)
	t.start()
