import sys

"""
굳이 처음에 입력받은 숫자를 사용하려면
슬라이싱 정도..?
"""

num = int(sys.stdin.readline())
number = sys.stdin.readline().rstrip('\n')
sum_ = 0
for i in number[:num]:
    sum_ += int(i)
print(sum_)
