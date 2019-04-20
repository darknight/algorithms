# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = current = None
        carry = 0
        while l1 or l2:
            if l1 and l2:
                val = l1.val + l2.val + carry
            elif l1:
                val = l1.val + carry
            elif l2:
                val = l2.val + carry
            else:
                break
            if val >= 10:
                carry = 1
                val -= 10
            else:
                carry = 0
            p = ListNode(val)
            if head is None:
                head = p
                current = p
            else:
                current.next = p
                current = p
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            current.next = ListNode(1)
        return head

if __name__ == '__main__':
    l1 = [ListNode(i) for i in range(3)]
    l1[0].val = 2
    l1[0].next = l1[1]
    l1[1].val = 4
    l1[1].next = l1[2]
    l1[2].val = 3

    l2 = [ListNode(0) for i in range(3)]
    l2[0].val = 5
    l2[0].next = l2[1]
    l2[1].val = 6
    l2[1].next = l2[2]
    l2[2].val = 8

    h = Solution().addTwoNumbers(l1[0], l2[0])
    while h:
        print h.val
        h = h.next
