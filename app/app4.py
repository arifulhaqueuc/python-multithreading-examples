import threading


def uf():
 print "Hello World"
 return

threads = []
t = threading.Thread(target=uf)
threads.append(t)
t.start()

