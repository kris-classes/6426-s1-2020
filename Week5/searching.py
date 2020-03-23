import random

random_list = [random.randint(1, 1000) for i in range(1000)]


def my_search(some_list, number):
    for i in range(len(random_list)):
        if some_list[i] == number:
            print('Found {} at index: {}'.format(number, i))

my_search(random_list, 532)