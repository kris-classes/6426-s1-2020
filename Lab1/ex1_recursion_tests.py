import pytest
import time
from ex1_recursion import *


print('=== Python Recursion Performance Tests ===')
print('NOTE: Understand how memoization works by studying these 2 examples.')
start = time.time()
recursive_fibonacci(36)
stop = time.time()
print(f'Slow naive recursive fibonacci time taken: {stop - start} seconds')
start = time.time()
recursive_memoization_fibonacci(36)
stop = time.time()
print(f'Fast identical recursive fibonacci using memoization time taken: {(stop - start):07f} seconds')

print('=== Recursion 1 Question ===')
print('Solve this problem: Testing recursion_base_case() function')
try:
    n = recursion_base_case(100, stop=95) #) == 95
except RecursionError:
    print('ERROR: You forgot to add a base-case to the recursion_base_case function. Do it for marks.')
else:
    if n == 95:
        print('Solved!')
    else:
        print(f'n == {n}. Keep trying!')

