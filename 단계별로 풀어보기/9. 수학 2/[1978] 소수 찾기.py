import sys


def find_decimal(num):
    cnt = 0
    for i in range(1, num+1):
        if num % i == 0:
            cnt += 1
    if cnt > 2:
        return False
    else:
        return True


if __name__ == "__main__":
    num = int(sys.stdin.readline().rstrip("\n"))
    num_list = list(map(int, sys.stdin.readline().rstrip('\n').split()))

    cnt = 0
    for i in num_list:
        if i != 1:
            if find_decimal(i):
                cnt += 1
    print(cnt)
