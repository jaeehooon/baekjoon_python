import sys


# 최대공약수 찾기 with 유클리드 호제법
def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


if __name__ == '__main__':
    _ = int(sys.stdin.readline())
    num_list = list(map(int, sys.stdin.readline().split()))
    bar = num_list[0]
    for num in num_list[1:]:
        gcd_val = gcd(bar, num)
        print("{}/{}".format(bar//gcd_val, num//gcd_val))
