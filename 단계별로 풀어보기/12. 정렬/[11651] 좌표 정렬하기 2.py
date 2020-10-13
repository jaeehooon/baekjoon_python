import sys


coord_list = list()
num = int(sys.stdin.readline())
for _ in range(num):
    element = list(map(int, sys.stdin.readline().rstrip('\n').split()))
    coord_list.append(element[::-1])

for coord in sorted(coord_list):
    coord = coord[::-1]
    print(coord[0], coord[1])
