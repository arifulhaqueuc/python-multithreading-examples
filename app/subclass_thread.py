import threading
import logging

logging.basicConfig(
	level=logging.DEBUG,
	format = '(%(threadName)-10s) %(message)s',
)


class FirstThread(threading.Thread):

    def run(self):
        logging.debug('This thread is running')
        return

for x in range(5):
	z=FirstThread()
	z.start()
