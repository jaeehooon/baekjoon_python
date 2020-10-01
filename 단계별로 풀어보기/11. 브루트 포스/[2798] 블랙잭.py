import sys


num, target = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().rstrip('\n').split()))
result = None
for i in range(num-2):
    for j in range(i + 1, num-1, 1):
        for k in range(j + 1, num, 1):
            tmp = numbers[i] + numbers[j] + numbers[k]
            if tmp <= target:
                if result is None:
                    result = tmp
                else:
                    if abs(target - tmp) < abs(target - result):
                        result = tmp

print(result)

"""
bisect : 이진 분할 알고리즘 학습해야함


"""

