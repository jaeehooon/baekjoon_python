import sys


def char_to_num(char):
    for i, charList in enumerate(num_list):
        if char in list(charList):
            return i + 1


def calc_time(input_str):
    sum_ = 0
    for a in input_str:
        sum_ += (char_to_num(a) + 1)
    return sum_


if __name__ == "__main__":
    num_list = ['', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ', '#']
    input_string = sys.stdin.readline().rstrip('\n')
    print(calc_time(input_string))
