# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        '''
        example:
        l1: 1 -> 3 -> 5 -> 9
        l2: 3 -> 5 -> 6
        '''
        if not all((l1, l2)):
            return l1 or l2
        if l1.val > l2.val:
            l1, l2 = l2, l1
        head = l1
        while l1 and l2:
            p = l1.next
            if p is None:
                l1.next = l2
                l2 = None
            else:
                if p.val <= l2.val:
                    l1 = p
                else:
                    q = l2
                    cursor = q.next
                    while cursor:
                        if cursor.val <= p.val:
                            q = cursor
                            cursor = cursor.next
                        else:
                            break
                    l1.next = l2
                    l2 = q.next
                    q.next = p
                    l1 = p
        return head

if __name__ == '__main__':
    node1 = ListNode(1)
    node3 = ListNode(3)
    node5 = ListNode(5)
    node9 = ListNode(9)
    node1.next = node3
    node3.next = node5
    node5.next = node9

    n3 = ListNode(3)
    n5 = ListNode(5)
    n6 = ListNode(6)
    n3.next = n5
    n5.next = n6

    #head = Solution().mergeTwoLists(node1, n3)
    head = Solution().mergeTwoLists(n3, node1)
    while head:
        print head.val
        head = head.next

