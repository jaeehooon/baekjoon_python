import sys


def bee(num):
    if num == 1:
        print(1)
    else:
        i = 1
        num_ = num - 1
        while True:
            num_ -= 6 * i

            if num_ <= 0:
                print(i + 1)
                break
            else:
                i += 1


if __name__ == "__main__":
    number = int(sys.stdin.readline())
    bee(number)
