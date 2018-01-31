## A Timer starts its work after a delay, 
## and can be canceled at any point within that delay time period.


#!/usr/bin/python
import threading
import time
import logging


logging.basicConfig(
	level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)


def delayed():
    logging.debug('Thread program still running')
    return

def Main():
	t1 = threading.Timer(3, delayed)
	t1.setName('Timer 1')
	t2 = threading.Timer(3, delayed)
	t2.setName('Timer 2')

	logging.debug('Starting thread timers')
	t1.start()
	t2.start()

	logging.debug('We are waiting before canceling %s', t2.getName())
	time.sleep(2)
	logging.debug('Now canceling %s', t2.getName())
	t2.cancel()


if __name__ == "__main__":
	Main()