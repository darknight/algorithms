#!/usr/bin/env python3

import math
import itertools
from collections import defaultdict
from typing import List
from typing import Set
try:
    from _tree import *
except ImportError:
    pass

try:
    from _list import *
except ImportError:
    pass

try:
    from _uitl import *
except ImportError:
    pass

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = -1
        while head is not None:
            if res == -1:
                res = head.val
            else:
                res = (res << 1) + head.val
            head = head.next

        return res

if __name__ == '__main__':
    pass
