import sys


x, y, w, h = list(map(int, sys.stdin.readline().rstrip('\n').split()))
abs_list = [abs(x-0), abs(w-x), abs(h-y), abs(y-0)]
print(min(abs_list))
