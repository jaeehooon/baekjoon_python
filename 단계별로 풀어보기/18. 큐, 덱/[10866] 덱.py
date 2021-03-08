import sys
from collections import deque


class MyDequeue(object):
    def __init__(self):
        self.dq = deque()

    def push_front(self, value):
        self.dq.appendleft(value)

    def push_back(self, value):
        self.dq.append(value)

    def size(self):
        return len(self.dq)

    def pop_front(self):
        if self.size() == 0:
            return -1
        return self.dq.popleft()

    def pop_back(self):
        if self.size() == 0:
            return -1
        return self.dq.pop()

    def empty(self):
        if self.size() == 0:
            return 1
        return 0

    def front(self):
        if self.size() == 0:
            return -1
        return self.dq[0]

    def back(self):
        if self.size() == 0:
            return -1
        return self.dq[-1]


if __name__ == '__main__':
    num_lines = int(sys.stdin.readline())
    dq = MyDequeue()
    for _ in range(num_lines):
        line = sys.stdin.readline().rstrip().split()

        if line[0] == 'push_back':
            dq.push_back(int(line[-1]))
        elif line[0] == 'push_front':
            dq.push_front(int(line[-1]))
        elif line[0] == 'pop_back':
            print(dq.pop_back())
        elif line[0] == 'pop_front':
            print(dq.pop_front())
        elif line[0] == 'size':
            print(dq.size())
        elif line[0] == 'empty':
            print(dq.empty())
        elif line[0] == 'front':
            print(dq.front())
        elif line[0] == 'back':
            print(dq.back())
