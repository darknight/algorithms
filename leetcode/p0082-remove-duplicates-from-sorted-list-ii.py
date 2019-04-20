#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # TODO: manipulate pointers
        if head is None or head.next is None:
            return head
        tmp = {}
        while head:
            val = head.val
            if val not in tmp:
                tmp[val] = [head]
            else:
                tmp[val].append(head)
            head = head.next
        keys = tmp.keys()
        keys.sort()
        h = None
        p = None
        for k in keys:
            nodes = tmp[k]
            if len(nodes) == 1:
                if h is None:
                    h = nodes[0]
                    h.next = None
                    p = h
                else:
                    p.next = nodes[0]
                    p = nodes[0]
                    p.next = None
        return h

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(1)
    node4 = ListNode(2)
    node5 = ListNode(3)
    #node6 = ListNode(4)
    #node7 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    #node5.next = node6
    #node6.next = node7
    h = Solution().deleteDuplicates(node1)
    while h:
        print(h.val)
        h = h.next
