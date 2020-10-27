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


if __name__ == '__main__':
    m = int(sys.stdin.readline().rstrip('\n'))
    n = int(sys.stdin.readline().rstrip('\n'))
    decimal_list = []
    for i in range(m, n+1):
        if i != 1:
            if find_decimal(i):
                decimal_list.append(i)
    if len(decimal_list) != 0:
        print(sum(decimal_list))
        print(min(decimal_list))
    else:
        print(-1)
