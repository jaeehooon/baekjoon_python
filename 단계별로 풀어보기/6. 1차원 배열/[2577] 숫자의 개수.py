import sys


num_list = [int(sys.stdin.readline()) for _ in range(3)]
val = str(num_list[0] * num_list[1] * num_list[2])
for i in range(10):
    print(val.count(str(i)))
