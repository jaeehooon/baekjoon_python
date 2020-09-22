import sys


"""
결과적으로는 입력된 순서는 고려하지 않아도 됐다.

"""
num = int(sys.stdin.readline())
customers = list()
for idx in range(num):
    age, name = list(sys.stdin.readline().rstrip('\n').split())
    customers.append((age, name, idx))

customers = sorted(customers, key=lambda customer: (customer[0], customer[2]))
for customer in customers:
    print(customer[0], customer[1])
