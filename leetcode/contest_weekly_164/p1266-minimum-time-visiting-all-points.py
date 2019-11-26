#!/usr/bin/env python3

import math
from collections import defaultdict
from typing import List
from typing import Set
try:
    from _tree import *
except ImportError:
    pass

try:
    from _uitl import *
except ImportError:
    pass


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        size = len(points)
        if size == 1:
            return 0

        res = 0
        for i in range(1, size):
            x0, y0 = points[i-1][0], points[i-1][1]
            x1, y1 = points[i][0], points[i][1]
            dx, dy = abs(x1-x0), abs(y1-y0)
            res += min(dx, dy) + abs(dx-dy)

        return res


if __name__ == '__main__':
    assert Solution().minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]) == 7
    assert Solution().minTimeToVisitAllPoints([[3,2],[-2,2]]) == 5
