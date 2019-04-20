#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        #TODO: slow & improve
        if m == n:
            return head
        length = n - m + 1
        prev = None
        h = head
        for i in range(1, m):
            prev = h
            h = h.next
        start = stop = h
        for i in range(length-1):
            curr = stop.next
            stop.next = curr.next
            curr.next = start
            start = curr
        if prev is None:
            return start
        else:
            prev.next = start
            return head

if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    h = Solution().reverseBetween(n1, 1, 5)
    while h:
        print(h.val)
        h = h.next
