import threading
import time
def callMeForEachThread(threadName, delay):
    counter = 0
    while counter<=5:
        print(threadName,"                  " , "Current Counter:",  counter)
        time.sleep(delay)
        counter+=1
        print(threadName, "                   Time: ", time.time())


if __name__ == "__main__":
    thread1 = threading.Thread(target=callMeForEachThread, args=("Thread 1", 1))
    thread2 = threading.Thread(target=callMeForEachThread, args=("Thread 2", 2))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


    print("Finished!")