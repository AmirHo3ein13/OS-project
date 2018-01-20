import os
from threading import Thread
import time


def n3_order_func(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                pass


def run(n, f, t):
    tm = time.time()

    for i in range(f):
        parent = os.fork()
        if not parent:
            threads = []
            for j in range(t):
                threads.append(Thread(target=n3_order_func, args=(n,)))

            for thr in threads:
                thr.start()

            for thr in threads:
                thr.join()

            exit()

    if parent:
        for i in range(f):
            os.waitpid(-1, 0)
        return [n, f, t, time.time() - tm]
