import sys


def fibonacci(n):
    if n < 0:
        return
    elif n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


num = int(sys.stdin.readline())
print(fibonacci(num))
