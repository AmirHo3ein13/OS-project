import os
from threading import Thread
# TODO: somewhere we should use time :)
import time


def n3_order_func(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                pass


class MyThread(Thread):
    def __init__(self, n):
        Thread.__init__(self)
        self.n = n

    def run(self):
        n3_order_func(self.n)


# n = number of executions
# f = number of processes
# t = number of threads
n, f, t = [int(x) for x in input().split()]

for i in range(f):
    # TODO: what should we do here?!?!
    os.fork()
    for j in range(t):
        th = MyThread(n)
        th.start()
