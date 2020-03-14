#!/usr/bin/env python3

import math, itertools, functools, heapq
from collections import defaultdict, Counter
from typing import List, Set, Dict, Tuple
try:
    from _tree import *
    from _list import *
    from _util import *
except ImportError:
    pass


class Solution:
    # slow solution
    def AC_mergeKLists(self, lists: List[ListNode]) -> ListNode:
        size = len(lists)
        if size == 0:
            return None
        if size == 1:
            return lists[0]
        head = ListNode(0)
        ptr = head
        while True:
            node = None
            val = math.inf
            idx = -1
            for i in range(size):
                if lists[i] is not None:
                    if lists[i].val < val:
                        node = lists[i]
                        val = lists[i].val
                        idx = i
            # no more nodes
            if node is None:
                break
            # append to new list
            ptr.next = node
            ptr = node
            lists[idx] = lists[idx].next

        return head.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nums = []
        for i in range(len(lists)):
            h = lists[i]
            while h is not None:
                nums.append(h.val)
                h = h.next

        nums.sort()
        if len(nums) == 0:
            return None
        head = ListNode(nums[0])
        ptr = head
        for val in nums[1:]:
            node = ListNode(val)
            ptr.next = node
            ptr = node

        return head


if __name__ == '__main__':
    pass
