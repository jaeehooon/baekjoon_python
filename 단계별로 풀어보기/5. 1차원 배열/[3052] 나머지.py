import sys


my_list = []
for i in range(10):
    my_list.append((int(sys.stdin.readline())) % 42)

print(len(set(my_list)))
