import sys


num = int(sys.stdin.readline())
for n in range(1, num+1):
    print("{}{}".format(" "*(num-n), ("*" * n)))
