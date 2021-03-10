import sys


def combination(n, r):
    if r == n or r == 0:
        return 1
    else:
        return combination(n, r - 1) * (n - r + 1) // r


if __name__ == '__main__':
    num_case = int(sys.stdin.readline())
    for _ in range(num_case):
        N, M = map(int, sys.stdin.readline().split())
        print(combination(M, N))
