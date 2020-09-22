import sys


num = int(sys.stdin.readline())
word_list = list()
for _ in range(num):
    word_list.append(sys.stdin.readline().rstrip('\n'))
for i in sorted(sorted(set(word_list)), key=len):
    print(i)

"""
다른 사람 풀이
- 출력할 때 for문을 돌리지 않고 아래와 같이 많이 씀
  print("\n".join(word_list))
  
  더 짧음
"""