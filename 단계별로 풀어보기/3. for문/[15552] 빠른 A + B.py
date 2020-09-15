import sys

num = int(sys.stdin.readline())
for _ in range(num):
    print(sum(list(map(int, sys.stdin.readline().split()))))
