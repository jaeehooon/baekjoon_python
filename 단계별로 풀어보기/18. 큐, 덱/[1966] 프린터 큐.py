import sys
from collections import deque


class Printout(object):
    """
    중요도를 속성으로 지니고 있는 출력물

    """
    def __init__(self, priority, index):
        self.priority = priority
        self.index = index

    def getPriority(self):
        return self.priority

    def getIndex(self):
        return self.index


class PrintDequeue(object):

    def __init__(self, inputs):
        self.dq = deque([Printout(input_, idx) for idx, input_ in enumerate(inputs)] )
        self.count = 0

    """
    yield 를 활용해서 풀 수도 있을 듯
    """
    def printOut(self, Mth):
        target = self.dq[Mth].priority
        while self.size() != 0:
            if self.maxIndex(self.max()) != 0:
                self.dq.append(self.dq.popleft())
            else:
                tmp_val = self.dq.popleft()
                if tmp_val.priority == target and tmp_val.index == Mth:
                    return self.count + 1

                self.count += 1

    def size(self):
        return len(self.dq)

    def max(self):
        max_val = -999999
        for element in self.dq:
            if element.priority >= max_val:
                max_val = element.priority
        return max_val

    def maxIndex(self, max_val):
        for idx, element in enumerate(self.dq):
            if element.priority == max_val:
                return idx


if __name__ == '__main__':
    lines = int(sys.stdin.readline())
    for _ in range(lines):
        N, M = map(int, sys.stdin.readline().split())               # N: 문서의 갯수, M: 몇 번째로 인쇄되었는지 궁금한 문서(0부터 시작)
        printDq = PrintDequeue(map(int, sys.stdin.readline().split()))
        if printDq.size() != N:
            print("갯수가 맞지 않습니다!")
            print(-1)
            continue
        print(printDq.printOut(M))









