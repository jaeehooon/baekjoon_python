import sys


coord = [None] * 2
for i in range(2):
    coord[i] = int(sys.stdin.readline().rstrip('\n'))

if (coord[0] > 0) and (coord[1] > 0):
    print(1)
elif (coord[0] > 0) and (coord[1] < 0):
    print(4)
elif (coord[0] < 0) and (coord[1] > 0):
    print(2)
else:
    print(3)
