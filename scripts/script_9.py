## This multithreading program prints output 
## of square and cube of a series of numbers


#!/usr/bin/python
import time
import threading


def PrintSquare(numbers):
  print("Print squares")
  for n in numbers:
    time.sleep(0.2)
    print("Square", n*n)


def PrintCube(numbers):
  print("Print cubes")
  for n in numbers:
    time.sleep(0.2)
    print("Cube", n*n*n)


def Main():
	arr = [2,3,4,5]
	t = time.time()
	PrintSquare(arr)
	PrintCube(arr)
	t1=threading.Thread(Target=PrintSquare, args=(arr,))
	t2=threading.Thread(Target=PrintCube, args=(arr,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print("Program took", time.time()-t)


if __name__ == '__main__':
	Main()


###################################################
###################################################
###################################################


## Above program has been written using multithreading module 
## and the following one has been written in conventional 
## way where threading module hasnot been used.
## A comparison between the above and folling program 
## would help the readers understand the difference 
## a normal program and a thread program.


# import time


# def PrintSquare(num):
#   print("Print squares of the given numbers")
#   for n in numbers:
#     time.sleep(0.2)
#     print("Square", n*n)


# def PrintCube(num):
#   print("Print cubes of the given numbers")
#   for n in numbers:
#     time.sleep(0.2)
#     print("Cube", n*n*n)


# arr = [2,3,4,5]
# t = time.time()
# PrintSquare(arr)
# PrintCube(arr)
# print("Program took", time.time()-t)
