import sys


def check(a, b):
    quotient = a // b
    remainder = a % b

    if quotient == 0 and remainder > 0:
        print("factor")
    elif quotient > 0 and remainder == 0:
        print("multiple")
    elif quotient != 0 and remainder != 0:
        print("neither")


if __name__ == "__main__":
    while True:
        a, b = map(int, sys.stdin.readline().split())
        if a == 0 and b == 0:
            break

        check(a, b)
