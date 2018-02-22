#!/usr/bin/python


# This program takes an string input from a user
# and print the input in a text file


import threading 
import time 


class AsyncWrite(threading.Thread):
  def __init__(self, text, out):
    threading.Thread.__init__(self)
    self.text = text
    self.out = out 

    
  def run(self):
    file = open(self.out, "a")
    file.write(self.text + '\n')
    file.close()
    time.sleep(2)
    print "Done! Completed storing input in a file named " + self.out 


def Main():
  message = raw_input("Enter a string: ")
  bg = AsyncWrite(message, 'out.txt')
  
  bg.start()
  print "Hold on, the program is generating a file"
  

if __name__ == '__main__':
  Main()
