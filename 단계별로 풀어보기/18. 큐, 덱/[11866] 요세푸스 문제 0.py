import sys
from collections import deque


class MyDeque(object):
    def __init__(self, size):
        self.dq = deque(i for i in range(1, size + 1))

    def remove(self, kth):
        for _ in range(kth - 1):
            self.dq.append(self.dq.popleft())
        return self.dq.popleft()

    def size(self):
        return len(self.dq)


if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    result = list()
    dq = MyDeque(N)
    while dq.size() != 0:
        result.append(dq.remove(K))
    print(str(result).replace("[", '<').replace("]", ">"))
