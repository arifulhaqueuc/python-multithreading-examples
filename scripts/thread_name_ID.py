#!/usr/bin/python


import threading
import time


class MyThread(threading.Thread):
    def run(self):
        print("{} started!".format(self.getName()))              # Thread-x started
        time.sleep(1)                                      
        print("{} finished!".format(self.getName()))             # Thread-x finished


def Main():
    for x in range(4):                                     
        mythread = MyThread(name = "Thread-{}".format(x + 1))  # Instantiate a thread and pass a unique ID to it
        mythread.start()
        time.sleep(1)   

        
if __name__ == '__main__':
	Main()
