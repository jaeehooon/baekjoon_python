import sys


def sum_each_num(num):
    return sum(map(int, list(str(num)))) + num


self_num_list = []
for i in range(1, 10000):
    self_num_list.append(sum_each_num(i))
    if i not in self_num_list:
        print(i)
