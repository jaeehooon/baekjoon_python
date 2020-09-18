import sys


num = int(sys.stdin.readline())
my_str = []
for i in range(num):
    input_str = sys.stdin.readline().rstrip('\n').split()
    my_str.append(input_str)

for j in my_str:
    for k in j[1]:
        print("{}".format(k * int(j[0])), end='')
    print()
