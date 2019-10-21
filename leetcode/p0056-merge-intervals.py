#!/usr/bin/env python3

import math
from collections import defaultdict
from typing import List
from typing import Set

try:
    from _tree import *
except ImportError:
    pass


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        size = len(intervals)
        intervals.sort(key=lambda x: x[0])

        res = [intervals[0]]
        for i in range(1, size):
            s1, e1 = res[-1][0], res[-1][1]
            s2, e2 = intervals[i][0], intervals[i][1]
            if s2 <= e1:
                res[-1] = [s1, max(e1, e2)]
            else:
                res.append([s2, e2])

        return res


if __name__ == '__main__':
    assert Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert Solution().merge([[1, 4], [4, 5]]) == [[1, 5]]

    # WA
    assert Solution().merge([[1, 4], [2, 3]]) == [[1, 4]]
