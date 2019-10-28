#!/usr/bin/env python3

import math
from collections import defaultdict
from typing import List
from typing import Set
try:
    from _tree import *
except ImportError:
    pass

class CustomFunction:
    # Returns f(x, y) for any given positive integers x and y.
    # Note that f(x, y) is increasing with respect to both x and y.
    # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
    def f(self, x, y):
        pass

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res = []
        for a in range(1, 1001):
            b = self.bsearch(z, a, a, 1000, customfunction)
            if b != -1:
                res.append([a, b])

        return res

    def bsearch(self, target: int, a: int, start: int, end: int, func: 'CustomFunction') -> int:

        while start <= end:
            mid = start + (end - start) // 2
            val = func.f(a, mid)
            if val == target:
                return mid
            elif val < target:
                start = mid + 1
            else:
                end = mid - 1

        return -1


if __name__ == '__main__':
    pass
