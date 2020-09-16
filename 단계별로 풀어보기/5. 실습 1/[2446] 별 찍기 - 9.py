import sys


num = int(sys.stdin.readline())
for i in range(1, 2*num, 1):
    if i <= num:
        print("{}{}".format(" "*(i-1), "*"*(2*num-2*i+1)))
    else:
        print("{}{}".format(" "*(2*num-1-i), "*"*(2*(i - num) + 1)))
