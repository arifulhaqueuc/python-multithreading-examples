import threading 
import time 

class AsyncWrite(threading.Thread):
  def __init__(self, text, out):
    threading.Thread.__init__(self)
    self.text = text
    self.out = out 
    
  def run(self):
    f = open(self.out, "a")
    f.write(self.text + '\n')
    f.close()
    time.sleep(2)
    print "Finished background file writing" + self.out 
    
def Main():
  message = raw_input("Enter a string to store: ")
  bg = AsyncWrite(message, 'out.txt')
  
  bg.start()
  print "The program can continue"
  
  print 100+300
  bg.join()
  print "Waited until thread was completed"
  
if __name__ == '__main__':
  Main()