import sys


def is_huge(A, B):
    return (A[0] > B[0]) and (A[1] > B[1])


if __name__ == '__main__':
    bulks = []
    num = int(sys.stdin.readline())
    for i in range(num):
        bulks.append(list(map(int, sys.stdin.readline().split())))

    for i in range(len(bulks)):
        count = 0
        for j in range(len(bulks)):
            if bulks[i] != bulks[j] and is_huge(bulks[j], bulks[i]):
                count += 1

        if count == 0:
            print(1, end=" ")
        else:
            print(count+1, end=" ")
