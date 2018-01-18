# n = 129 and 645
import os
from threading import Thread
import time


def n3_order_func(n, number):
    # print('Thread number = ', number, '\tprocess id = ', os.getpid())
    for i in range(n):
        for j in range(n):
            for k in range(n):
                pass


# n = number of executions
# f = number of processes
# t = number of threads

n, f, t = [int(x) for x in input().split()]
# n, f, t = 100, 2, 95

tm = time.time()

# p_threads = dict()
for i in range(f):
    parent = os.fork()
    if not parent:
        threads = []
        for j in range(t):
            # print('make thread ', j)
            threads.append(Thread(target=n3_order_func, args=(n, j)))
        # counter = 1
        for thr in threads:
            # print('start thread ', counter)
            # counter += 1
            thr.start()
        # counter = 1
        for thr in threads:
            # print('join thread ', counter)
            # counter += 1
            thr.join()

        exit()
    # else:
    #     print('Process id = ', os.getpid())


if parent:
    for i in range(f):
        os.waitpid(-1, 0)
    print('\033[94m', time.time() - tm, '\033[0m')

