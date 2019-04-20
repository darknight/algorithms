#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        '''two stages:
        1.check if linked list has a cycle
        2.take overlapped node as end node, the problem becomes:
        if two linked lists overlap, find first overlap node
        '''
        if head is None or head.next is None:
            return None
        if head.next.next is None:
            return None
        slow = head.next
        fast = head.next.next
        cycled = False
        while True:
            if fast.next is None:
                break
            if fast.next.next is None:
                break
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                cycled = True
                break
        if not cycled:
            return None
        # is cycled, break up from current node
        # TODO: some sort of verbose, recode later
        end_point = slow
        start1 = slow.next
        start2 = head
        size1 = 0
        size2 = 0
        while start1 is not end_point:
            size1 += 1
            start1 = start1.next
        while start2 is not end_point:
            size2 += 1
            start2 = start2.next
        start1 = slow.next
        start2 = head
        if size1 > size2:
            size = size1 - size2
            start1 = slow.next
            while size:
                start1 = start1.next
                size -= 1
        elif size1 < size2:
            size = size2 - size1
            start2 = head
            while size:
                start2 = start2.next
                size -= 1
        while start1 is not start2:
            start1 = start1.next
            start2 = start2.next
        return start1

if __name__ == '__main__':
    nodes = [ListNode(i) for i in range(7)]
    head = nodes[0]
    nodes[0].next = nodes[1]
    nodes[1].next = nodes[0]
    print(Solution().hasCycle(head).val)

    for i in range(6):
        nodes[i].next = nodes[i+1]
    print(Solution().hasCycle(head))
    nodes[-1].next = nodes[3]
    print(Solution().hasCycle(head).val)
