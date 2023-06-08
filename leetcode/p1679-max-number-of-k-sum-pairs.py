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
    def maxOperations(self, nums: List[int], k: int) -> int:
        valid = [n for n in nums if n < k]
        count = defaultdict(int)
        for n in valid:
            count[n] += 1

        res = 0
        for n in valid:
            pair = k - n
            if n == pair and count[n] >= 2:
                res += 1
                count[n] -= 2
            if n != pair and count[n] >= 1 and count[pair] >= 1:
                res += 1
                count[n] -= 1
                count[k-n] -= 1

        return res


if __name__ == '__main__':
    pass
