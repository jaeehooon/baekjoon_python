import sys


num = sys.stdin.readline().rstrip('\n')
print(''.join(sorted(num, reverse=True)))
