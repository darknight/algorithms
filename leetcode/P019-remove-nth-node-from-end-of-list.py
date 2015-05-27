# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        h = head
        t = None

        for i in xrange(n):
            h = h.next
        t = head

        while h and h.next is not None:
            h = h.next
            t = t.next

        if h is None:
            return head.next
        else:
            t.next = t.next.next
            return head

if __name__ == '__main__':
    nodes = [ListNode(i+1) for i in range(5)]
    nodes[0].next = nodes[1]
    #nodes[1].next = nodes[2]
    #nodes[2].next = nodes[3]
    #nodes[3].next = nodes[4]

    def print_list(h):
        vals = []
        while h:
            vals.append(str(h.val))
            h = h.next
        print '->'.join(vals)

    #print_list(nodes[0])
    #print_list(Solution().removeNthFromEnd(nodes[0], 2))
    #print_list(Solution().removeNthFromEnd(nodes[0], 1))
    #print_list(Solution().removeNthFromEnd(nodes[0], 5))
    print_list(Solution().removeNthFromEnd(nodes[0], 1))
