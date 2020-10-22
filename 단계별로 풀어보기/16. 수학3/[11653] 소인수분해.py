import sys


num = int(sys.stdin.readline())
idx = 2
while num > 1:
    # 코드 추가
    if idx > num**0.5:
        print(num)
        break
    if num % idx == 0:
        print(idx)
        num //= idx
    else:
        idx += 1

"""
다른 사람의 풀이

- idx 가 n**0.5 보다 크면 이후에는 소인수가 존재하지 않는다.
- 따라서 끝까지 갈 필요없이 종료하면됨
"""
