import sys


def combination(n, r):
    if r == 0 or r == n:
        return 1
    else:
        return combination(n, r-1) * (n - r + 1) // r


def num_resident(floor, room):
    return combination(room + floor, room - 1)


if __name__ == "__main__":
    num = int(sys.stdin.readline())
    for _ in range(num):
        f = int(sys.stdin.readline().rstrip('\n'))
        r = int(sys.stdin.readline().rstrip('\n'))
        print(num_resident(f, r))
