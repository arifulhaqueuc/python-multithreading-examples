## This is not very trivial to access the values of 
## args and kwargs from a subclass as their values are
## being saved in private variables. 

import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

class ThreadWithArgs(threading.Thread):

    def __init__(self, 
                group=None, 
                target=None, 
                name=None,
                args=(), 
                kwargs=None, 
                verbose=None
                ):
        threading.Thread.__init__(
            self, 
            group=group, 
            target=target, 
            name=name,
            verbose=verbose
        )
        
        self.args = args
        self.kwargs = kwargs
        return

    def run(self):
        logging.debug('This thread is running with %s and %s', self.args, self.kwargs)
        return

for x in range(10):
    z = ThreadWithArgs(args=(x,), kwargs={'Country':'USA', 'Zip':'12345'})
    z.start()
