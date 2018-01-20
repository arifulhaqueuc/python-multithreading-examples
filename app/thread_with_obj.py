#!/usr/bin/env python

from __future__ import print_function       #should be on the top
import threading
import time


class MyThread(threading.Thread):
    def run(self):
        print("{} started!".format(self.getName()))              # "Thread-x started!"
        time.sleep(1)                                      # Pretend to work for a second
        print("{} finished!".format(self.getName()))             # "Thread-x finished!"

if __name__ == '__main__':
    for x in range(4):                                     # Four times...
        mythread = MyThread(name = "Thread-{}".format(x + 1))  # ...Instantiate a thread and pass a unique ID to it
        mythread.start()                                   # ...Start the thread
        time.sleep(.9)                                     # ...Wait 0.9 seconds before starting another
        