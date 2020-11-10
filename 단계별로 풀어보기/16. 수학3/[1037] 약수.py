import sys

"""
약수 확인 코드
"""
# def get_factors(number):
#     result = list()
#     for num in range(1, int(number**0.5) + 1):
#         if number % num == 0:
#             result.append(num)
#             if (number // num) not in result:
#                 result.append(number // num)
#
#     return sorted(result)
#
#
# if __name__ == '__main__':
#     # input_number = int(sys.stdin.readline())
#     for num in range(1, 201):
#         factors = get_factors(num)
#         print("num: {:3d},\t진짜 약수 갯수 : {:2d},\t{}".format(num, len(factors)-2, factors))


if __name__ == '__main__':
    num_factors = int(sys.stdin.readline())
    factors = list(map(int, sys.stdin.readline().split()))

    if num_factors >= 2:
        print(min(factors) * max(factors))
    else:
        print(factors[0]**2)
