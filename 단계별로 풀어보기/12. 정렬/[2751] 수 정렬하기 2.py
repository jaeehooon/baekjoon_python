import sys


"""
내가 푼 풀이
"""
num = int(sys.stdin.readline())
num_list = list()
for _ in range(num):
    num_list.append(int(sys.stdin.readline()))

sorted_list = sorted(num_list)
for i in sorted_list:
    print(i)


"""
다른 사람 풀이
- stdout을 통해 출력
- 파이참에서는 입력받는 부분에서 계속 입력을 받게됨...
"""
from sys import stdin, stdout

input()
arr = sorted(map(int, stdin.read().split()))
stdout.write('\n'.join(map(str,arr)))