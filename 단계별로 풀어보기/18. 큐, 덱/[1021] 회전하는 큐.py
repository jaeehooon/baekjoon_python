import sys
from collections import deque


class CircleQueue(object):

    def __init__(self, size):
        self.size = size
        self.dq = deque(list(i for i in range(1, N + 1)))
        self.count = 0

    def moveLeft(self):
        self.dq.append(self.dq.popleft())

    def moveRight(self):
        self.dq.appendleft(self.dq.pop())

    def getSize(self):
        return self.size

    def run(self, numbers):

        def find_index(number):
            for idx, n in enumerate(self.dq):
                if n == number:
                    return idx

        for num in numbers:
            if self.dq[0] != num:
                idx = find_index(num)
                size = self.getSize()
                if idx > (size // 2):
                    for _ in range(size - idx):
                        self.moveRight()
                        self.count += 1
                else:
                    for _ in range(idx):
                        self.moveLeft()
                        self.count += 1

            self.dq.popleft()
            self.size -= 1

        return self.count


if __name__ == '__main__':
    N, target = map(int, sys.stdin.readline().split())
    numbers = list(map(int, sys.stdin.readline().split()))
    cq = CircleQueue(N)
    print(cq.run(numbers))
