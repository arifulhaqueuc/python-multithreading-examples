import time


def square(numbers):
  print("Print squares")
  for n in numbers:
    time.sleep(0.2)
    print("Square", n*n)

def cube(numbers):
  print("Print cubes")
  for n in numbers:
    time.sleep(0.2)
    print("Cube", n*n*n)

arr = [2,3,4,5]
t = time.time()
square(arr)
cube(arr)
print("Program took", time.time()-t)
