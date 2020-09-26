import sys

"""
내가 푼 풀이
"""
num = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().rstrip('\n').split()))
print(min(numbers), max(numbers))

"""
다른 사람풀이

- *를 이용
- 결국엔 파이썬에서는 처음받는 num(숫자의 갯수)은 무의미..!
- 근데 아래의 방식은 파이참에서는 실행안됨...
"""
a, *b = map(int, sys.stdin.read().split())
print(min(b), max(b))


