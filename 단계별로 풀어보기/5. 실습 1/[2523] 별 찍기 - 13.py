import sys


num = int(sys.stdin.readline())
for i in range(1, 2*num, 1):
    print("*"*i if i <= num else "*"*(2*num-i))
