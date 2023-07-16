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
    def deleteMiddle_2_passes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 0
        p = head
        while p is not None:
            size += 1
            p = p.next

        if size == 1:
            return None

        middle = size // 2
        i = 0
        prev = None
        curr = head
        while i < middle:
            prev = curr
            curr = curr.next
            i += 1

        prev.next = curr.next
        curr.next = None
        return head

    # TODO: 2 pointers
    def deleteMiddle_2_pointers(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass


if __name__ == '__main__':
    pass
