import sys


num = int(sys.stdin.readline())
lines = []

for i in range(num):
    lines.append(sys.stdin.readline().rstrip('\n'))

for line in lines:
    total = 0
    abroad_avg = 0

    line = line.split()
    line = [int(v) for v in line]

    avg_value = (sum(line[1:]) / int(line[0]))

    for j in range(1, len(line)):
        if int(line[j]) > avg_value:
            abroad_avg += 1

    print("{:5.3f}%".format((abroad_avg / int(line[0])) * 100))
