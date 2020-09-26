import sys


num_list = [int(sys.stdin.readline()) for _ in range(9)]
max_val = max(num_list)
print(max_val)
print(num_list.index(max_val)+1)
