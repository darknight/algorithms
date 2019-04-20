# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None or k < 0:
            return head
        n = 0
        h = head
        t = None
        while h:
            n += 1
            t = h
            h = h.next

        k = k % n
        if k == 0:
            return head

        h = head
        skip = n - k - 1
        while skip:
            h = h.next
            skip -= 1
        t.next = head
        head = h.next
        h.next = None
        return head

if __name__ == '__main__':
    nodes = [ListNode(i) for i in range(1, 6)]
    for i in range(4):
        nodes[i].next = nodes[i+1]
    head = nodes[0]
    head = Solution().rotateRight(head, 5)
    while head:
        print head.val
        head = head.next
