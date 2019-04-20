# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def _isPalindrome(self, head):
        # FIXME:
        '''
        maybe exceed max recursive depth
        '''
        if head == None or head.next == None:
            return True

        isValid = [True]
        h = [head]

        def _next(node):
            #nonlocal isValid
            #nonlocal head
            if node.next == None:
                # the last node
                if h[0].val != node.val:
                    isValid[0] = False
            else:
                _next(node.next)
                h[0] = h[0].next
                if h[0].val != node.val:
                    isValid[0] = False

        _next(head)
        return isValid[0]

    def isPalindrome(self, head):
        '''
        refer to:
        https://leetcode.com/discuss/49900/
        accepted-reverse-second-half-list-compare-wth-the-first-half
        '''
        if head == None or head.next == None:
            return True

        n = 1
        p = head
        while p.next:
            n += 1
            p = p.next
        tail = p

        if n == 2:
            if head.val == tail.val:
                return True
            return False

        mid = n / 2
        p = head
        while mid:
            p = p.next
            mid -= 1
        q = p.next
        while q:
            r = q.next
            q.next = p
            p = q
            q = r

        mid = n / 2
        while mid:
            if head.val != tail.val:
                return False
            else:
                head = head.next
                tail = tail.next
                mid -= 1
        return True

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    print Solution().isPalindrome(node1)

