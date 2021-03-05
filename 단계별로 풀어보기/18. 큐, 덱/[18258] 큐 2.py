import sys
from collections import deque

'''
리스트로 구현했을 시, 시간 초과
따라서 모듈 사용
'''


class MyDequeue(object):
    def __init__(self):
        self.dq = deque()

    def push(self, value):
        self.dq.append(value)

    def pop(self):
        if len(self.dq) == 0:
            return -1
        return self.dq.popleft()

    def empty(self):
        if len(self.dq) == 0:
            return 1
        return 0

    def size(self):
        return len(self.dq)

    def front(self):
        if len(self.dq) == 0:
            return -1
        return self.dq[0]

    def back(self):
        if len(self.dq) == 0:
            return -1
        return self.dq[-1]


if __name__ == '__main__':
    num_line = int(sys.stdin.readline())
    dq = MyDequeue()
    for _ in range(num_line):
        line = sys.stdin.readline().rstrip().split()

        if line[0] == 'push':
            dq.push(int(line[-1]))
        elif line[0] == 'pop':
            print(dq.pop())
        elif line[0] == 'size':
            print(dq.size())
        elif line[0] == 'empty':
            print(dq.empty())
        elif line[0] == 'front':
            print(dq.front())
        elif line[0] == 'back':
            print(dq.back())
