import sys


num = int(sys.stdin.readline())
num_list = list()
for _ in range(num):
    num_list.append(int(sys.stdin.readline()))

sorted_list = sorted(num_list)
for i in sorted_list:
    print(i)
