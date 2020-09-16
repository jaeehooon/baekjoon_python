"""
입력이 끝날때까지 A+B를 출력하는 문제.
EOF에 대해 알아 보세요.

EOF는 빈 문자열, 예를 들면 "" 같은 문자열
아래의 코드에서 아무 입력이 없으면 예외처리가 되어 종료가 됨
"""
import sys

while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
    except:
        break
    print(a + b)
