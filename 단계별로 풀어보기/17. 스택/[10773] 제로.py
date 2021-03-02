import sys


class Stack(object):
    """
    문제 10828번의 스택을 이용

    """
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def top(self):
        if len(self.stack) == 0:
            return False
        return self.stack[len(self.stack) - 1]

    def pop(self):
        if len(self.stack) == 0:
            return False
        return self.stack.pop()

    def sum(self):
        return sum(self.stack)


if __name__ == '__main__':
    num_line = int(sys.stdin.readline())
    stack = Stack()
    for _ in range(num_line):
        number = int(sys.stdin.readline())

        if number != 0:
            stack.push(number)
        else:
            stack.pop()

    print(stack.sum())
