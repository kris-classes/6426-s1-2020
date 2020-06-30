"""
Kamho Szeto
Assignment Task 1:
Implementation of binary search
"""
import random

random_list = [random.randint(0, 2**15) for i in range(2**15)]

def search_the_list(the_list):
    """get a value to search for"""
    the_list.sort()
    print(the_list)
    print('list length:', len(the_list))
    search_for = int(input('looking for number in list:'))
    search(the_list, search_for, len(the_list) // 2)

def search(current_list, search_for, position_in_list):
    """check if the searching value is higher or lower than the mid point"""

    midpoint_index = len(current_list) // 2
    mid_var = current_list[midpoint_index]

    print('list:', current_list)
    print('midpoint index:{}'.format(midpoint_index))
    print('mid var:{}'.format(mid_var))
    print('position in list index:', position_in_list)


    if search_for < mid_var:
        print('{} < {} go to left list'.format(search_for, mid_var))
        search_from_list = current_list[:midpoint_index]
        position_in_list -= len(search_from_list) - len(search_from_list) // 2

    elif search_for > mid_var:
        print('{} > {} go to right list'.format(search_for, mid_var))
        search_from_list = current_list[midpoint_index+1:]
        position_in_list += len(search_from_list) // 2 + 1

    else:
        print('search for number:{}'.format(search_for))
        print('found!')
        print('your number is found at index {} of the list'.format(position_in_list))
        return


    if search_for != mid_var and len(search_from_list) > 0:
        search(search_from_list, search_for, position_in_list)
    else: # if the searching number is not in the list, stop recursion
        print('number not found in list')


search_the_list(random_list)
