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
    def reverseList_iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        new_head = None
        while head is not None:
            p = head.next
            if new_head is None:
                new_head = head
                new_head.next = None
            else:
                head.next = new_head
                new_head = head
            head = p

        return new_head

    def reverseList_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        res = [None]

        def reverse(node: ListNode) -> ListNode:
            if node.next is None:
                res[0] = node
                return node
            curr = node
            tail = reverse(node.next)
            tail.next = curr
            curr.next = None
            return curr

        reverse(head)
        return res[0]


if __name__ == '__main__':
    pass
