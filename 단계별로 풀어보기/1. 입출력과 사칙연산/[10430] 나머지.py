import sys


num1, num2, num3 = map(int, sys.stdin.readline().split())
print((num1 + num2) % num3)
print(((num1 % num3) + (num2 % num3)) % num3)
print((num1 * num2) % num3)
print(((num1 % num3) * (num2 % num3)) % num3)
