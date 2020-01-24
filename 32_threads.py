"""
thread as smallest unit of execution!
multithreading

thread module (depreceated) (python 3+ has _thread to support backward compatibility!)
threading module

"""

import _thread
import time


def callMeForEachThread(threadName, delay):
    counter = 0
    while counter<=5:
        print(threadName,"                  " , "Current Counter:",  counter)
        time.sleep(delay)
        counter+=1
        print(threadName, "                   Time: ", time.time())
# function being called by main thread!
#callMeForEachThread("Thread 1", 1)

_thread.start_new_thread(callMeForEachThread, ("Thread 1", 1))
_thread.start_new_thread(callMeForEachThread, ("Thread 2", 2))
_thread.start_new_thread(callMeForEachThread, ("Thread 3", 3))
_thread.start_new_thread(callMeForEachThread, ("Thread 4", 4))

input()

#fuoco


