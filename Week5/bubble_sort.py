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
one_million_items = [random.randint(1,100) for i in range(1000000)]

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
bubble_sort(ten_thousand_items)

start = time.time()
my_list = sorted(ten_items)
stop = time.time()
print('TimSort: time taken for 10 items: {}'.format(stop - start))

start = time.time()
my_list = sorted(one_hundred_items)
print('TimSort: time taken for 100 items: {}'.format(stop - start))
stop = time.time()

start = time.time()
my_list = sorted(one_thousand_items)
stop = time.time()
print('TimSort: time taken for 1000 items: {}'.format(stop - start))

start = time.time()
my_list = sorted(ten_thousand_items)
stop = time.time()
print('TimSort: time taken for 10000 items using sorted(): {}'.format(stop - start))

start = time.time()
my_list = ten_thousand_items.sort()
stop = time.time()
print('TimSort: time taken for 10000 items using list.sort(): {}'.format(stop - start))

start = time.time()
my_list = sorted(one_million_items)
stop = time.time()
print('TimSort: time taken for 1 million items using sorted(): {}'.format(stop - start))

start = time.time()
my_list = one_million_items.sort()
stop = time.time()
print('TimSort: time taken for 1 million items using list.sort(): {}'.format(stop - start))
