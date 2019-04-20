#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return None
        if head and head.next is None:
            return head
        left_head = None
        left_tail = None
        right_head = None
        right_tail = None
        p = head
        while p:
            q = p.next
            if p.val < x:
                if left_head is None:
                    left_head = left_tail = p
                else:
                    left_tail.next = p
                    left_tail = p
                left_tail.next = None
            else:
                if right_head is None:
                    right_head = right_tail = p
                else:
                    right_tail.next = p
                    right_tail = p
                right_tail.next = None
            p = q

        if left_tail is None:
            return right_head
        else:
            left_tail.next = right_head
            return left_head

if __name__ == '__main__':
    nodes = [ListNode(i) for i in range(5)]
    #nodes[0].next = nodes[3]
    #nodes[3].next = nodes[2]
    #nodes[2].next = nodes[1]
    #nodes[1].next = nodes[4]
    nodes[2].next = nodes[1]
    h = Solution().partition(nodes[2], 1)
    while h:
        print(h.val)
        h = h.next

