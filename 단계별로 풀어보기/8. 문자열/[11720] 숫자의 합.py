import sys


num = int(sys.stdin.readline())
number = sys.stdin.readline().rstrip('\n')
sum_ = 0
for i in number:
    sum_ += int(i)
print(sum_)
