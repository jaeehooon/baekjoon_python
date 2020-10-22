import sys


def factorial(number):
    temp = 1
    if number <= 1:
        return 1

    for i in range(1, number + 1, 1):
        temp *= i
    return temp


if __name__ == '__main__':
    num = int(sys.stdin.readline())
    value = str(factorial(num))[::-1]
    count = 0

    for i in value:
        if i == '0':
            count += 1
        else:
            break
    print(count)

"""
다른 사람 풀이

- print(num//5 + num//25 + num//125) (...?)

"""
