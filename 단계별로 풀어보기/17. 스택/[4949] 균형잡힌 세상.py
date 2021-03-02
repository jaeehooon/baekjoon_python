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

    def size(self):
        return len(self.stack)

    def clear(self):
        self.stack.clear()


def check_parenthesis_string(stack, string):
    for c in string:

        if c in ['(', '{', '[', ')', '}', ']']:
            if c == '(' or c == '[' or c == '{':
                stack.push(c)
            else:
                if c == ')' and stack.top() == '(' \
                    or (c == ']' and stack.top() == '[') \
                        or (c == '}' and stack.top() == '{'):
                    stack.pop()
                else:
                    stack.push(c)

    if stack.size() == 0:
        return True
    return False


if __name__ == '__main__':
    s = Stack()
    while True:
        s.clear()
        line = sys.stdin.readline().rstrip('\n')
        if line == '.':
            break
        if check_parenthesis_string(s, line):
            print("yes")
        else:
            print("no")
