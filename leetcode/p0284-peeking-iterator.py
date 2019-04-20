#!/usr/bin/env python3

# Below is the interface for Iterator, which is already defined for you.
#
class Iterator(object):
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.data = nums

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return len(self.data) > 0

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        return self.data.pop(0)

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.head = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.head is None:
            self.head = self.iterator.next()
        return self.head

    def next(self):
        """
        :rtype: int
        """
        if self.head is None:
            return self.iterator.next()
        res = self.head
        if self.iterator.hasNext():
            self.head = self.iterator.next()
        else:
            self.head = None
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        has = self.iterator.hasNext()
        if has or self.head:
            return True
        return False

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
if __name__ == '__main__':
    for i in range(5):
        nums = range(i)
        iter = PeekingIterator(Iterator(nums))
        while iter.hasNext():
            val = iter.peek()
            n = iter.next()
            print(val == n)
