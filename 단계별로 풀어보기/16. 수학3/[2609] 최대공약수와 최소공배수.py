import sys


# 최대공약수 찾기 with 유클리드 호제법
def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def lcm(c, d):
    gcd_val = gcd(c, d)
    return gcd_val * (c // gcd_val) * (d // gcd_val)


if __name__ == '__main__':
    num_a, num_b = map(int, sys.stdin.readline().rstrip('\n').split())
    print(gcd(num_a, num_b))
    print(lcm(num_a, num_b))
