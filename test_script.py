from os_module import run

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
            times.append(run(n, f, t))
            print(times[-1])

        with open('result-%d-%d.json' % (n, num), 'w') as f:
            for t in times:
                f.write(','.join(t) + '\n')
