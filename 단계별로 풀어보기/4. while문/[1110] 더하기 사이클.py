import sys


def _cycle(number):
    num_0, num_1 = number[0], number[1]
    temp = "{:2d}".format(int(num_0) + int(num_1))
    return num_1 + temp[1]


def cycle(input_number):
    number = input_number
    count = 0
    while True:
        number = _cycle(number)
        count += 1
        if number == input_number:
            break
    return count


if __name__ == "__main__":
    input_ = "{:02d}".format(int(sys.stdin.readline()))
    print(cycle(input_))
