import sys


num = int(sys.stdin.readline())
for _ in range(num):
    a, b = map(int, sys.stdin.readline().rstrip('\n').split())
    print(a + b)
