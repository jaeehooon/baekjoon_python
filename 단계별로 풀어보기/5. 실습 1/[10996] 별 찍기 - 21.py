import sys


def _rotate(num):
    for i in range(1, num+1):
        print("{}".format("*" if i % 2 == 1 else " "), end='')
    print()
    for i in range(1, num+1):
        print("{}".format("*" if i % 2 == 0 else " "), end='')


def rotate(num):
    for i in range(1, num+1):
        _rotate(num)
        print()


if __name__ == "__main__":
    number = int(sys.stdin.readline())
    rotate(number)
