import sys

"""
내가 푼 풀이
"""
input_ = sys.stdin.readline().rstrip('\n')
input_set = set(input_)
for i in range(ord('a'), ord('z') + 1):
    i = chr(i)
    if i in input_set:
        print(input_.index(i), end=' ')
    else:
        print(-1, end=' ')

"""
다른 사람 풀이 1
"""
input_ = sys.stdin.readline().rstrip('\n')
chars = "abcdefghijklmnopqrstuvwxyz"
for i in chars:
    print(input_.find(i), end=' ')

"""
다른 사람 풀이 2
"""
chars = [-1] * 26        # 이용하여 인덱싱을 통한 풀이

