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
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        head, tail = toBeRemoved[0], toBeRemoved[1]
        for interval in intervals:
            h, t = interval[0], interval[1]
            if t <= head or h >= tail:
                res.append(interval)
                continue
            if h < head and t > tail:
                res.append([h, head])
                res.append([tail, t])
                continue
            if h < head and t < tail:
                res.append([h, head])
                continue
            if h < tail and t > tail:
                res.append([tail, t])
                continue

        print(res)
        return res


if __name__ == '__main__':
    Solution().removeInterval(intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6])
    Solution().removeInterval(intervals = [[0,5]], toBeRemoved = [2,3])
