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
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        count = defaultdict(int)
        max_len = 0
        for rec in rectangles:
            edge = min(rec)
            count[edge] += 1
            max_len = max(max_len, edge)

        return count[max_len]


if __name__ == '__main__':
    print(Solution().countGoodRectangles([[5,8],[3,9],[5,12],[16,5]]))
    print(Solution().countGoodRectangles([[2,3],[3,7],[4,3],[3,7]]))
