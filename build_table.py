import os


for file in os.listdir('results/'):
    with open('results/' + file) as f:
        data = [x[:-1].split(',') for x in f.read().split('\n')[:-1]]

    min_time = float(data[0][3])
    index = 0
    for row in data:
        if float(row[3]) < min_time:
            min_time = float(row[3])

    print('Exec', 'Proc', 'Threads', 'Time', sep='\t')
    for row in data:
        check = False
        if row[3] == str(min_time):
            print('\033[93m', end='')
            check = True
        for element in row:
            print(element, end='\t')
        if check:
            print('\033[0m', end='')
        print()
    print('\n')

