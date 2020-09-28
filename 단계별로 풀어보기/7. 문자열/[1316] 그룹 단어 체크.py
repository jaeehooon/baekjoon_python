import sys


def group_check(input_str):
    num_gc = []

    for i, char in enumerate(input_str):
        if input_str[i+1:].find(char) not in [-1, 0]:
            return 0
        else:
            continue
    return 1


if __name__ == "__main__":
    num = int(sys.stdin.readline().rstrip("\n"))
    str_list = []

    for i in range(num):
        str_list.append(sys.stdin.readline().rstrip("\n"))

    group_num = 0
    for each_str in str_list:
        if group_check(each_str):
            group_num += 1
    print(group_num)
