# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head is None or head.next is None:
            return False
        if head.next.next is None:
            return False
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
            if slow == fast:
                cycled = True
                break
        return cycled

if __name__ == '__main__':
    nodes = [ListNode(i) for i in range(7)]
    for i in range(6):
        nodes[i].next = nodes[i+1]
    head = nodes[0]
    print Solution().hasCycle(head)
    nodes[-1].next = nodes[3]
    print Solution().hasCycle(head)
