import sys
import math


def uclid_circle(r):
    return math.pi * (r**2)


def taxi_circle(r):
    return 2*(r**2)


if __name__ == '__main__':
    r = int(sys.stdin.readline())
    print(uclid_circle(r))
    print(taxi_circle(r))
