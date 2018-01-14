import os
from threading import Thread
import time


def n3_order_func(n, number):
    print('Thread number = ', number, '\tprocess id = ', os.getpid())
    for i in range(n):
        for j in range(n):
            for k in range(n):
                pass


# n = number of executions
# f = number of processes
# t = number of threads

# n, f, t = [int(x) for x in input().split()]
n, f, t = 1000, 2, 95

tm = time.time()

# TODO: fix termination problem
p_threads = dict()
for i in range(f):
    parent = os.fork()
    if not parent:
        p_threads[os.getpid()] = []
        for j in range(t):
            print('make thread ', j)
            p_threads[os.getpid()].append(Thread(target=n3_order_func, args=(n, j)))
        counter = 1
        for thr in p_threads[os.getpid()]:
            print('start thread ', counter)
            counter += 1
            thr.start()
        counter = 1
        for thr in p_threads[os.getpid()]:
            print('join thread ', counter)
            counter += 1
            thr.join()
    else:
        print('Process id = ', os.getpid())


time.sleep(100)
print(time.time() - tm)

