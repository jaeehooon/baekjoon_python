import sys
from collections import deque


class MyDeque(object):
    def __init__(self, capacity):
        self.dq = deque(i for i in range(1, capacity + 1))

    def faceToDown(self):
        tmp = self.dq.popleft()
        self.dq.append(tmp)

    def discard(self):
        self.dq.popleft()

    def size(self):
        return len(self.dq)

    def pop(self):
        return self.dq.pop()


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    dq = MyDeque(n)
    while dq.size() != 1:
        dq.discard()
        dq.faceToDown()
    print(dq.pop())
