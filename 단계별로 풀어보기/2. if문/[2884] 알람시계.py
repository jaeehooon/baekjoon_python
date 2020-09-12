import sys


h, m = map(int, sys.stdin.readline().rstrip('\n').split())

if ((h < 0) or (h > 23)) and ((m < 0) or (m > 59)):
    print("다시 입력하세요!")
else:
    if h == 0:
        m -= 45
        if m < 0:
            m += 60
            hour = 23
    else:
        m -= 45
        if m < 0:
            m += 60
            h -= 1

    print(h, min)
