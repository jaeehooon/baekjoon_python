import sys


def count_min_bag(n):
    loc_list = []
    try:
        num = max(n//5, n//3)+1
    except:
        return -1
    for y in range(num):
        for x in range(num):
            if n == 5*x + 3*y :
                loc_list.append([x, y])

    if len(loc_list) == 0:
        return -1

    min_ = 50000
    for e in loc_list:
        if sum(e) < min_:
            min_ = sum(e)

    return min_


if __name__ == "__main__":
    kg = int(sys.stdin.readline().rstrip('\n'))
    print(count_min_bag(kg))
