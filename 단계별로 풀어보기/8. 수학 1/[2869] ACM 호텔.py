import sys


"""
내가 푼 풀이
"""
def assign_room(h, w, n):
    count = 0
    for i in range(1, w + 1, 1):
        for j in range(1, h + 1, 1):
            count += 1
            if count == n:
                print("{}{:02d}".format(j, i))


"""
다른 사람 풀이

- q = N // H + 1
- r = N % H + 1 

이런식으로 의미를 따져서 구함
"""


if __name__ == "__main__":
    num = int(sys.stdin.readline())
    for _ in range(num):
        h, w, n = map(int, sys.stdin.readline().rstrip('\n').split())
        assign_room(h, w, n)
