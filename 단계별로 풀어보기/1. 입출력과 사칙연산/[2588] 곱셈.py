import sys


num1 = int(sys.stdin.readline())
num2 = int(sys.stdin.readline())
for num in reversed(str(num2)):
    print(num1 * int(num))
print(num1 * num2)
