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
    from _uitl import *
except ImportError:
    pass


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        size = len(intervals)
        if size == 1:
            return 1
        intervals.sort(key=lambda x: (x[0], -x[1]))
        i = 0
        while i < len(intervals):
            head, tail = intervals[i][0], intervals[i][1]
            j = i + 1
            while j < len(intervals):
                h, t = intervals[j][0], intervals[j][1]
                if h >= tail:
                    break
                if t <= tail:
                    intervals.pop(j)
                    continue
                j += 1
            i += 1

        return len(intervals)


if __name__ == '__main__':
    assert Solution().removeCoveredIntervals([[1,4],[3,6],[2,8]]) == 2
    assert Solution().removeCoveredIntervals([[1,4],[1,6],[2,8]]) == 2
    assert Solution().removeCoveredIntervals([[1,4],[2,4],[2,8]]) == 2
    assert Solution().removeCoveredIntervals([[1,4],[4,5],[7,8]]) == 3
