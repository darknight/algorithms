#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None:
            return None
        p = head
        q = p.next
        while p and q:
            if p.val == q.val:
                p.next = q.next
                q = q.next
            else:
                p = p.next
                q = q.next
        return head

if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(1)
    n3 = ListNode(2)
    n4 = ListNode(3)
    n5 = ListNode(3)

    n1.next = n2
    n2.next = n3
    #n3.next = n4
    #n4.next = n5

    print('before:')
    p = n1
    while p:
        print(p.val)
        p = p.next
    root = Solution().deleteDuplicates(n1)
    print('after:')
    p = root
    while p:
        print(p.val)
        p = p.next

