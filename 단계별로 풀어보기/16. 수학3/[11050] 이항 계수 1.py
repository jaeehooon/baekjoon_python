import sys


def combination(n, k):
    if (k > n) or (k < 0):
        return 0

    if n - k <= k:
        k = n - k
    result = 1
    for i in range(n, n - k, -1):
        result *= (i / (i - (n - k)))

    """
    위의 코드에서
    combination 에서 int 로 캐스팅하여 반환하면 파이썬 부동소숫점 문제때문에 8C3 등이 문제가 생김
    따라서 round 로 취해주어 반환함
    """
    return round(result)


if __name__ == '__main__':
    a, b = map(int, sys.stdin.readline().split())
    print(combination(a, b))

    # for a in range(1, 11, 1):
    #     for b in range(0, a + 1, 1):
    #         print("{}C{} >>> {}".format(a, b, combination(a, b)))
