import random
import time
import random

start = time.time()

my_list = [5, 2, 4, 3, 1]
sorted_list = [1, 2, 3, 4, 5]
reversed_list = [5, 4, 3, 2, 1]

random_list = [random.randint(1,100) for i in range(100)]

def bubble_sort(data):
    start = time.time()
    print('bubble_sort')
    passes, comparisons, swaps = 0, 0, 0
    n = len(data)
    for j in range(n - 1):
        passes += 1
        for i in range(n - j - 1):
            comparisons += 1
            current, next = data[i], data[i+1]
            if current > next:
                swaps += 1
                print('{} > {}. Swap them'.format(current, next))
                data[i], data[i+1] = next, current
    print('Sorted: {}'.format(data))
    print('Passes: {} - Comparisons: {} - Swaps: {}'.format(passes, comparisons, swaps))
    stop = time.time()
    print('Time Taken: {} seconds'.format(stop - start))


bubble_sort(random_list)

stop = time.time()
timedTaken = stop - start
print(f'It took {timed}')

