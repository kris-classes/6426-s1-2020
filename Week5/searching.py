import random

random_list = [random.randint(1, 1000000) for i in range(1000000)]


def my_search(some_list, number):
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

my_search(random_list, 532325)

#for i in range(1000):
#    random_list = [random.randint(1, 1000000) for i in range(1000000)]
#    my_search(random_list, 532325)
