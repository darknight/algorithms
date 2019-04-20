# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def _insertionSortList(self, head):
        '''
        Time Limit Exceeded
        '''
        if head is None or head.next is None:
            return head
        new_head = head
        head = head.next
        new_head.next = None
        while head:
            q = head
            head = head.next
            q.next = None
            p = new_head
            if p.val > q.val:
                q.next = p
                new_head = q
                continue
            while p and p.next:
                if p.val <= q.val < p.next.val:
                    q.next = p.next
                    p.next = q
                    break
                else:
                    p = p.next
            if p.next is None:
                p.next = q
        return new_head

    #TODO: speedup this solution
    def insertionSortList(self, head):
        if head is None or head.next is None:
            return head
        new_head = head
        head = head.next
        new_head.next = None
        new_tail = new_head
        while head:
            q = head
            head = head.next
            q.next = None
            if new_head.val >= q.val:
                q.next = new_head
                new_head = q
                continue
            if new_tail.val <= q.val:
                new_tail.next = q
                new_tail = q
                continue
            p = new_head
            while p and p.next:
                if p.val <= q.val < p.next.val:
                    q.next = p.next
                    p.next = q
                    break
                else:
                    p = p.next
            if p.next is None:
                p.next = q
        return new_head

if __name__ == '__main__':
    import random
    n = 5
    nodes = [ListNode(random.randint(1, 100)) for i in range(n)]
    #nodes = [ListNode(i) for i in range(n)]
    for i in range(n-1):
        nodes[i].next = nodes[i + 1]
    print 'before sort'
    head = nodes[0]
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print res
    new_head = Solution().insertionSortList(nodes[0])
    print 'afert sort'
    res2 = []
    while new_head:
        res2.append(new_head.val)
        new_head = new_head.next
    print res2

