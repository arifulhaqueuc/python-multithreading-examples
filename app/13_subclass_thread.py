#!/usr/bin/python


import threading
import logging
import time


logging.basicConfig(
	level=logging.DEBUG,
	format = '(%(threadName)-10s) %(message)s',
)


class MyThread(threading.Thread):
    def run(self):
        logging.debug('This thread is running')
        return

for x in range(5):
	z=MyThread()
	z.start()
	time.sleep(1)        
        
        
