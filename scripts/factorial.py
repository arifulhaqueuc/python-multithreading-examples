#!/usr/bin/python


##1. Calculate factorial using recursion.
##2. Call factorial function using thread. 


from thread import start_new_thread

threadId = 1


def factorial(n):
   global threadId
   if n < 1:   # base case
       print "%s: %d" % ("Thread", threadId )
       threadId += 1
       return 1
   else:
       returnNumber = n * factorial( n - 1 )  # recursive call
       print(str(n) + '! = ' + str(returnNumber))
       return returnNumber

start_new_thread(factorial,(5, ))
start_new_thread(factorial,(4, ))

c = raw_input("Waiting for threads to return...\n")
