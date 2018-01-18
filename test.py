import os
from threading import Thread
import time


def n3_order_func(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                pass


iter_counts = (129, 645)

nums = [190, 210, 1024]
forms = {x: list() for x in nums}
for num in nums:
    for i in range(1, num + 1):
        if not num % i:
            forms[num].append(tuple([i, int(num / i)]))

for n in iter_counts:
    for num in nums:
        times = []
        for f, t in forms[num]:
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
                times.append([n, f, t, time.time() - tm])
                print(times[-1])

        with open('result-%d-%d.json' % (n, num), 'w') as f:
            for t in times:
                for el in t:
                    f.write(str(el) + ',')
                f.write('\n')
