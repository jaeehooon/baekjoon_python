"""
두 원의 관계를 나타내는 문제
"""

import sys


def count_integer(r1, r2):
    """
    두 원 사이의 관계를 나타내는 메소드
    두 원이 겹치게 되면 교점이 2개 생기고
    접하면 교점이 1개,
    겹치지 않으면 교점이 0개인 문제로 변환됨

    :param r1:      원 1
    :param r2:      원 2
    :return:        교점의 개수
    """
    if r1[:2] != r2[:2]:
        if abs(r1[2] - r2[2]) < ((r1[0] - r2[0])**2 + (r1[1] - r2[1])**2)**(1/2) < abs(r1[2] + r2[2]):
            return 2
        elif (((r1[0] - r2[0])**2 + (r1[1] - r2[1])**2)**(1/2) == abs(r1[2] + r2[2])) or \
                (((r1[0] - r2[0])**2 + (r1[1] - r2[1])**2)**(1/2) == abs(r1[2] - r2[2])):
            return 1
        else:
            return 0
    else:
        if r1[2] != r2[2]:
            return 0
        else:
            return -1


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    for _ in range(n):
        two_circles = list(map(int, sys.stdin.readline().rstrip('\n').split()))
        r1_circle = two_circles[:3]
        r2_circle = two_circles[3:]
        print(count_integer(r1_circle, r2_circle))
