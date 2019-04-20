#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        p = head
        q = head.next
        p.next = q.next
        q.next = p
        head = q
        h = head.next
        p = h.next
        if p is None:
            return head
        q = p.next
        while p and q:
            p.next = q.next
            q.next = p
            h.next = q
            h = p
            p = p.next
            if p is None:
                break
            q = p.next
        return head

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7

    head = Solution().swapPairs(node1)
    while head:
        print(head.val)
        head = head.next

