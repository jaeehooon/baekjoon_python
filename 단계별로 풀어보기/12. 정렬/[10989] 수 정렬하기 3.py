import sys


num = int(sys.stdin.readline())
num_list = [int(sys.stdin.readline()) for _ in range(num)]
for i in sorted(num_list):
    print(i)
