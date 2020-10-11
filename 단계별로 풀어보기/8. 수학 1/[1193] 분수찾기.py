import sys


def get_range(number):
    sum_ = 0
    num_ = number
    for i in range(1, number+1):
        num_ -= i
        sum_ += i
        if num_ <= 0:
            return i, sum_ - number


if __name__ == "__main__":
    num = int(sys.stdin.readline())

    idx, val = get_range(num)
    if idx % 2 == 0:
        print("{}/{}".format(idx-val, val+1))
    else:
        print("{}/{}".format(val+1, idx-val))
