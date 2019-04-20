#!/usr/bin/env python3

class Stack:
    # initialize your data structure here.
    def __init__(self):
        from collections import deque
        self.queue = deque()

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.queue.append(x)

    # @return nothing
    def pop(self):
        count = len(self.queue) - 1
        while count:
            temp = self.queue.popleft()
            self.queue.append(temp)
            count -= 1
        self.queue.popleft()

    # @return an integer
    def top(self):
        count = len(self.queue) - 1
        while count:
            temp = self.queue.popleft()
            self.queue.append(temp)
            count -= 1
        res = self.queue[0]
        temp = self.queue.popleft()
        self.queue.append(temp)
        return res

    # @return an boolean
    def empty(self):
        return len(self.queue) == 0


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    print(s.top() == 2)
    s.pop()
    print(s.top() == 1)
    print(s.empty() == False)
    s.push(3)
    print(s.top() == 3)
    s.pop()
    s.pop()
    print(s.empty() == True)

