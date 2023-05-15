from threading import Semaphore, Thread
import time

sem: Semaphore = Semaphore()
stop_threads = False


def fun1():
    while not stop_threads:
        sem.acquire()
        print(1)
        sem.release()
        time.sleep(0.25)


def fun2():
    while not stop_threads:
        sem.acquire()
        print(2)
        sem.release()
        time.sleep(0.25)


t1: Thread = Thread(target=fun1)
t2: Thread = Thread(target=fun2)

try:
    t1.start()
    t2.start()
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print('\nReceived keyboard interrupt, quitting threads.')
    stop_threads = True
    t1.join()
    t2.join()
    exit(1)
