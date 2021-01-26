import sys


num = int(sys.stdin.readline())
number = 0
count = 0
while True:
    number += 1
    if "666" in str(number):
        count += 1
        if count == num:
            print(number)
            break
