### Background

As we all know, in general, running multiple threads simulteneously is equivalent to running several programs at the same time. In such case, threading in Python is a very popular process to attain concurrency and parallelism. Using threading module in a Python program gives us several key advatages such as sharing same data space and operating on light-weight process in order to avoid unnecessary memory overhead. 

This repository helps us understand usage of Python's threading module in different programs with various requirements. 


### Project Overview
|  |  |
| --- | --- |
| Repo Type | Scripts |
| Status | Phase 1 |
| Development Timeline | Start Jan 2018 :: Finish Feb 2018 |

### Project Description

**hello_world.py**

This is a simple program to print Hello World using threading. A user defined function is created and the function is called when a thread has been initialized.


**add_number.py**

This program adds two numbers and prints the result with thread.


**for_loop.py**

This program creates five threads which in turn each will print "Hello World" on the screen.


**five_threads_prallel.py**

This program creates five threads which executed in parallel, each of them will add two numbers and will print the results.


**acquired_lock.py**

**square_cube.py**

**square_cube_v2.py**

**timer_example.py**

**timer_with_loop.py**


### Support / Found a bug?
Here are the options

(1) Please file an issue with detailed description.

(2) If you know a possible solution, please create a new brnach, update the code and then submit pull request.

(3) If you would  like to reach out to me directly with any question, email me at ariful.haque.uc@gmail.com
  
### General Disclaimer 
This is my personal repo and not an official product of any company. If you would like to use this code, please keep it in your mind that, although I have tried to make it as error-free as possible, there's no warranty of a 100% bug free application. 
