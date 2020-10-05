import sys


def prime_list(lower, upper):
    num_list = [True] * (upper+1)
    num_list[0], num_list[1] = False, False

    for i in range(2, int(upper ** 0.5) + 1):
        if num_list[i] == True:
            for j in range(i + i, upper+1, i):
                num_list[j] = False
    return [i for i in range(lower, upper+1) if num_list[i] == True]


if __name__ == "__main__":
    while True:
        n = int(sys.stdin.readline())
        if n == 0:
            break
        print(len(prime_list(n+1, 2*n)))
