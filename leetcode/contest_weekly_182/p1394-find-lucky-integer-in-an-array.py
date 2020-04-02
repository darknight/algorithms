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
    def findLucky(self, arr: List[int]) -> int:
        res = [0] * 501
        for num in arr:
            res[num] += 1
        for i in range(500, 0, -1):
            if i == res[i]:
                return i
        return -1

if __name__ == '__main__':
    pass
