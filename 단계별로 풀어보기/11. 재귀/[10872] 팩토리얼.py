import sys


def factorials(n):
    if n < 2:
        return 1
    else:
        return n * factorials(n-1)


if __name__ == "__main__":
    num = int(sys.stdin.readline())
    print(factorials(num))
