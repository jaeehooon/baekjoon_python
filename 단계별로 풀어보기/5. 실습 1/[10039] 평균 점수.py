import sys


scores = []
for _ in range(5):
    num = int(sys.stdin.readline())
    if num < 40:
        num = 40
    scores.append(num)
print(int(sum(scores) / len(scores)))
