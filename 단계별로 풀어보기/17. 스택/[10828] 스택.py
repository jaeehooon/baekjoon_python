import sys


class Stack(object):

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

    def size(self):
        return len(self.stack)

    def empty(self):
        return bool(len(self.stack) == 0)


if __name__ == '__main__':
    num_line = int(sys.stdin.readline())
    stack = Stack()
    for _ in range(num_line):
        line = sys.stdin.readline().split()

        if line[0] == 'push':
            stack.push(int(line[-1]))
        elif line[0] == 'top':
            val = stack.top()
            if val is False:
                print(-1)
            else:
                print(val)
        elif line[0] == 'pop':
            val = stack.pop()
            if val is False:
                print(-1)
            else:
                print(val)
        elif line[0] == 'size':
            print(stack.size())
        elif line[0] == 'empty':
            if stack.empty():
                print(1)
            else:
                print(0)
