import random
import time

n = int(input('Enter Number: '))

presorted_list = [i for i in range(n)]
# A presorted list
reversed_list = [i for i in range(n, 0, -1)]
# A reversed list
random_list = presorted_list.copy()
random.shuffle(random_list)
# A randomly shuffled list
duplicates_list = [random.randint(1, 10) for i in range(n)]
# A list containing many duplicates


def mSort(listItem):
    print(f'Length of list is: {len(listItem)}')
    # print(f'Initial list is: {listItem}')
    startTime = time.perf_counter()
    comparisons = 0
    swaps = 0

    def sort(listItem, compare, swap):
        if len(listItem) > 1:
            mid = len(listItem) // 2
            lefthalf = listItem[:mid]
            #print(f'left half{lefthalf}')
            righthalf = listItem[mid:]
            #print(f'right half{righthalf}')
            sort(lefthalf, compare, swap)
            sort(righthalf, compare, swap)
            i = j = k = 0
            while i < len(lefthalf) and j < len(righthalf):
                compare += 1
                # print('comparison')
                if lefthalf[i] < righthalf[j]:
                    swap += 1
                    listItem[k] = lefthalf[i]
                    i = i + 1

                else:
                    listItem[k] = righthalf[j]
                    swap += 1
                    # print('swap')
                    j = j + 1
                k = k + 1

            while i < len(lefthalf):
                listItem[k] = lefthalf[i]
                i = i + 1
                k = k + 1

            while j < len(righthalf):
                listItem[k] = righthalf[j]
                j = j + 1
                k = k + 1
            return listItem, compare, swap

    finishTime = time.perf_counter()
    finishTime = finishTime - startTime
    data = sort(listItem, comparisons, swaps)
    swaps = data[2]
    comparisons = data[1]
    print(f'Sorted list is: {listItem}')
    print(f'Number of items swapped:{swaps}')
    print(f'Number of items compared:{comparisons}')
    print(f'Time taken: {finishTime}\n')


print('Presorted list')
mSort(presorted_list)

print('Reversed list')
mSort(reversed_list)

print('Random list')
mSort(random_list)

print('Duplicates list')
mSort(duplicates_list)

input('done')
