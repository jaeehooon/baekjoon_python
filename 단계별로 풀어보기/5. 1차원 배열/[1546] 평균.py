import sys


num = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

sum_value = 0
for j in num_list:
    sum_value += j / (max(num_list))*100

print(sum_value/num)
