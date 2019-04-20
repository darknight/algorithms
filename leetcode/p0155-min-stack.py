class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []
        self.index = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack.append(x)
        if len(self.index) == 0:
            self.index.append(0)
        else:
            min_index = self.index[-1]
            if self.stack[min_index] <= x:
                self.index.append(min_index)
            else:
                self.index.append(len(self.stack) - 1)

    # @return nothing
    def pop(self):
        self.stack.pop()
        self.index.pop()

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        return self.stack[self.index[-1]]

if __name__ == '__main__':
    s = MinStack()
    s.push(5)
    print s.getMin()
    s.push(6)
    print s.getMin()
    s.push(4)
    print s.getMin()
    s.push(7)
    print s.getMin()
    s.push(1)
    print s.getMin()
