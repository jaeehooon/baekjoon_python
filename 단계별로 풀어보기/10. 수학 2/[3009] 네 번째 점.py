import sys


x_list, y_list = list(), list()
for _ in range(3):
    a, b = (map(int, sys.stdin.readline().rstrip('\n').split()))
    x_list.append(a)
    y_list.append(b)

x_set, y_set = list(set(x_list)), list(set(y_list))
x, y = 0, 0

for i in x_set:
    count = x_list.count(i)
    if count == 1:
        x = i
for j in y_set:
    count = y_list.count(j)
    if count == 1:
        y = j

print(x, y)
