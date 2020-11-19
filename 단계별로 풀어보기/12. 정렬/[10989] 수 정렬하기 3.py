import sys


num = int(sys.stdin.readline())
result = [0] * 10001
for _ in range(num):
    n = int(sys.stdin.readline())
    result[n] += 1

"""
내가 푼 풀이
"""
for i in range(10001):
    if result[i] != 0:

        if result[i] != 1:
            for j in range(result[i]):
                print(i)
        else:
            print(i)


"""
문자열 출력 풀이
"""

for i, n in enumerate(result):
    if n >= 1:
        print("{}\n".format(i) * n, end='')
