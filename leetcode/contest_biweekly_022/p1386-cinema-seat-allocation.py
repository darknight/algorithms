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
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        """
        TLE if loop from 1 to n
        TLE if loop from 1 to n and pop reserved seats inside the loop
        """
        cache = defaultdict(int)
        for seat in reservedSeats:
            row, col = seat[0], seat[1]
            cache[row] = cache[row] | (1 << (10 - col))

        res = 0
        for reserved in cache.values():
            if reserved & 0b0111111110 == 0:
                res += 2
            elif reserved & 0b0111100000 == 0:
                res += 1
            elif reserved & 0b0000011110 == 0:
                res += 1
            elif reserved & 0b0001111000 == 0:
                res += 1

        return res + (n-len(cache)) * 2



if __name__ == '__main__':
    pass
