import sys

"""
내가 푼 풀이
"""
coord_list = list()
num = int(sys.stdin.readline())
for _ in range(num):
    coord_list.append(list(map(int, sys.stdin.readline().rstrip('\n').split())))

for coord in sorted(coord_list):
    print(coord[0], coord[1])


"""
다른 사람들 풀이
- stdin, stdout을 이용
- 대부분 문제에서 수의 범위가 주어진 경우, 예를 들어 1,000,000,000 이하의 숫자 등과 같은 조건이 있을 때
  [None] * 1000000000 (또는 1000000001) 이렇게 많이함. 공부할 필요있음
"""