import random

# Linearly through list

random_list = [random.randint(1, 1000000) for i in range(1000000)]


print('Linear Search')
print('===')
def linear_search(some_list, number):
    print('Starting search')
    position = 0
    for i in range(len(random_list)):
        position += 1
        if some_list[i] == number:
            break

    if position == len(some_list):
        print('{} not found'.format(number))
    else:
        print('Found {} at index: {}'.format(number, i))

linear_search(random_list, 532325)

# Sort the list first
random_list.sort()
linear_search(random_list, 5)

random_list.sort(reverse=True)
linear_search(random_list, 990000)
#for i in range(1000):
#    random_list = [random.randint(1, 1000000) for i in range(1000000)]
#    linear_search(random_list, 532325)


#Merge Sort and list divisibility

random_list = [random.randint(1, 10) for i in range(10)]
small_list = [5, 7, 3, 4, 4, 9, 2, 1, 0, 9, 8, 1933]
#random_list.sort()

print('Binary Search 1')
print('===')
def binary_search1(some_sorted_list, number):
    midpoint = len(some_sorted_list) // 2  # Floor Division
    midpoint_item = some_sorted_list[midpoint]
    print('midpoint item: {}'.format(midpoint_item))
    if number < midpoint_item:
        print('number is on the left')
        print('left list: {}'.format(some_sorted_list[midpoint - 5:midpoint]))
    else:
        print('number is on the right')
        print('right list: {}'.format(some_sorted_list[midpoint:midpoint + 5]))

binary_search1(random_list, 7)
# REMEMBER TO SORT YOUR LIST
small_list.sort()
binary_search1(small_list, 7)

# Without recursion base case
def binary_search2(some_sorted_list, number):
    midpoint = len(some_sorted_list) // 2  # Floor Division
    midpoint_item = some_sorted_list[midpoint]
    print('midpoint item: {}'.format(midpoint_item))
    if number < midpoint_item:
        left_list = some_sorted_list[:midpoint]
        print('number is on the left')
        print('left list: {}'.format(some_sorted_list[midpoint - 5:midpoint]))
        binary_search2(left_list, number)
    else:
        right_list = some_sorted_list[midpoint:]
        print('number is on the right')
        print('right list: {}'.format(some_sorted_list[midpoint:midpoint + 5]))
        binary_search2(right_list, number)

small_list.sort()
# Note: Max Recursion Depth. Run as an exercise.
# binary_search2(small_list, 7)


def binary_search3(some_sorted_list, number):
    if len(some_sorted_list) == 1:
        print('final list: {}'.format(some_sorted_list))
        print('Found number: {}'.format(number))
        return 'hooray!'

    midpoint = len(some_sorted_list) // 2  # Floor Division
    midpoint_item = some_sorted_list[midpoint]
    print('midpoint item: {}'.format(midpoint_item))
    if number < midpoint_item:
        left_list = some_sorted_list[:midpoint]
        print('number is on the left')
        print('left list: {}'.format(some_sorted_list[midpoint - 5:midpoint]))
        binary_search3(left_list, number)
    else:
        right_list = some_sorted_list[midpoint:]
        print('number is on the right')
        print('right list: {}'.format(some_sorted_list[midpoint:midpoint + 5]))
        binary_search3(right_list, number)

small_list.sort()
binary_search3(small_list, 7)

#for i in range(1000):
#    random_list = [random.randint(1, 1000000) for i in range(1000000)]
#    linear_search(random_list, 532325)
