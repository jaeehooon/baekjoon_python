import sys


prices = list(map(int, (sys.stdin.readline() for _ in range(5))))
print(min(prices[:3]) + min(prices[3:]) - 50)
