import time

my_list = [5, 2, 4, 3, 1]

def bubble_sort(data):
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

bubble_sort(my_list)

