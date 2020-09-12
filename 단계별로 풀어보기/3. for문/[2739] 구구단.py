import sys


a = int(sys.stdin.readline())
for i in range(9):
    print("{} * {} = {}".format(a, (i+1), a*(i+1)))
