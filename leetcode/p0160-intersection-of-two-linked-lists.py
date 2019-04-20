# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        lenA = 1
        lenB = 1
        pa = headA
        pb = headB
        while pa.next is not None:
            lenA += 1
            pa = pa.next
        while pb.next is not None:
            lenB += 1
            pb = pb.next
        if pa is not pb:
            return None
        pa = headA
        pb = headB
        if lenA > lenB:
            for _ in range(lenA - lenB):
                pa = pa.next
        if lenA < lenB:
            for _ in range(lenB - lenA):
                pb = pb.next
        while pa is not pb:
            pa = pa.next
            pb = pb.next
        return pa

if __name__ == '__main__':
    ls0 = [ListNode(i) for i in range(4)]
    ls1 = [ListNode(i) for i in range(1)]
    ls0[0].next = ls0[1]
    ls0[1].next = ls0[2]
    ls0[2].next = ls0[3]
    ls1[0].next = ls0[2]
    ha = ls0[0]
    hb = ls1[0]
    res = Solution().getIntersectionNode(ha, hb)
    print res.val


