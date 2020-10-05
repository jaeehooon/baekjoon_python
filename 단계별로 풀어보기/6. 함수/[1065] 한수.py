import sys


def hansoo(number):
    count = 0
    for i in range(1, number + 1):
        number_list = list(str(i))

        my_list = []
        if i < 10:
            count += 1
        else:
            for j in range(len(number_list) - 1):
                my_list.append(int(number_list[j]) - int(number_list[j + 1]))

            my_set = set(my_list)
            if len(my_set) == 1:
                count += 1
    return count


if __name__ == "__main__":
    number = int(sys.stdin.readline().rstrip('\n'))
    print(hansoo(number))
