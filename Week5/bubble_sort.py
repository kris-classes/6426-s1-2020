import random
import time
import random

my_list = [5, 2, 4, 3, 1]
sorted_list = [1, 2, 3, 4, 5]
reversed_list = [5, 4, 3, 2, 1]

ten_items = [random.randint(1,100) for i in range(10)]
one_hundred_items = [random.randint(1,100) for i in range(100)]
one_thousand_items = [random.randint(1,100) for i in range(1000)]
ten_thousand_items = [random.randint(1,100) for i in range(10000)]
one_hundred_thousand_items = [random.randint(1,100) for i in range(100000)]

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
                #print('{} > {}. Swap them'.format(current, next))
                data[i], data[i+1] = next, current
    #print('Sorted: {}'.format(data))
    print('Passes: {} - Comparisons: {} - Swaps: {}'.format(passes, comparisons, swaps))
    stop = time.time()
    print('Time Taken: {} seconds'.format(stop - start))


bubble_sort(ten_items)
bubble_sort(one_hundred_items)
bubble_sort(one_thousand_items)
