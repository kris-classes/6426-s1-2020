from functools import lru_cache


@lru_cache(maxsize=100)
def fibonacci(n):
    if type(n) != int:
        raise TypeError("n must be a positive number")
    if n < 1:
        raise ValueError("n must be a positive number")
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(1, 101):
    print(i, ";", fibonacci(i))

# def fibonacci(n):
#    if n in fibonacciCache:
#        return fibonacciCache[n]
#    if n == 1:
#        return 1
#    elif n == 2:
#        return 2
#    elif n > 2:
#        value = fibonacci(n-1) + fibonacci(n-2)
#        fibonacciCache[n] = value
#        return value
# fibonacciCache = {}
