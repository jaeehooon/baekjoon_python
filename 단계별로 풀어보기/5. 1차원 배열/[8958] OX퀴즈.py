import sys


num = int(input())
lines = []

for i in range(num):
    lines.append(sys.stdin.readline().rstrip('\n'))

for line in lines:
    o_count = 0
    total = 0

    for j in range(len(line)):
        o_count += 1

        if line[j] == 'O':
            total += o_count
        else:
            o_count = 0
    print(total)
