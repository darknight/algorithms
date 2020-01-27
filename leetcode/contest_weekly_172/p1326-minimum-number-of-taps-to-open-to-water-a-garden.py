#!/usr/bin/env python3

import math, itertools
from collections import defaultdict, Counter
from typing import List, Set, Dict

try:
    from _tree import *
    from _list import *
    from _util import *
except ImportError:
    pass


class Solution:
    def TLE_minTaps(self, n: int, ranges: List[int]) -> int:
        res = [-1]

        def dfs(i: int, area: (int, int), open_taps: int):
            if area[0] <= 0 and area[1] >= n:
                if res[0] == -1:
                    res[0] = open_taps
                else:
                    res[0] = min(res[0], open_taps)
            if i > n:
                return
            # skip current tap
            dfs(i + 1, area, open_taps)
            # open current tap
            low, high = i - ranges[i], i + ranges[i]
            if low <= area[1]:
                dfs(i + 1, (area[0], high), open_taps + 1)
            else:
                dfs(i + 1, (low, high), open_taps + 1)

        dfs(0, (0, 0), 0)
        return res[0]

    def AC_1_minTaps(self, n: int, ranges: List[int]) -> int:
        """
        refer to
        https://www.youtube.com/watch?v=G88X89Eo2C0

        similar to p1024
        """
        intervals = []
        for i, r in enumerate(ranges):
            intervals.append([i - r, i + r])

        intervals.sort(key=lambda x: x[0])

        res = 0
        i = 0
        last_end = 0
        while last_end < n:
            curr_end = last_end
            while i <= n and intervals[i][0] <= last_end:
                curr_end = max(curr_end, intervals[i][1])
                i += 1
            if curr_end == last_end:
                return -1
            res += 1
            last_end = curr_end

        return res

    def minTaps(self, n: int, ranges: List[int]) -> int:
        """
        refer to
        https://www.youtube.com/watch?v=G88X89Eo2C0

        similar to p0045
        """
        max_range = [0] * (n+1)
        for i, r in enumerate(ranges):
            left, right = max(0, i-r), min(n, i+r)
            max_range[left] = max(max_range[left], right)

        res = 0
        last_furthest = 0
        curr_furthest = 0
        for i in range(n+1):
            if i > curr_furthest:
                return -1
            if i > last_furthest:
                res += 1
                last_furthest = curr_furthest
            curr_furthest = max(curr_furthest, max_range[i])

        return res


if __name__ == '__main__':
    assert Solution().minTaps(n=5, ranges=[3, 4, 1, 1, 0, 0]) == 1
    assert Solution().minTaps(n=3, ranges=[0, 0, 0, 0]) == -1
    assert Solution().minTaps(n=7, ranges=[1, 2, 1, 0, 2, 1, 0, 1]) == 3
    assert Solution().minTaps(n=8, ranges=[4, 0, 0, 0, 0, 0, 0, 0, 4]) == 2
    assert Solution().minTaps(n=8, ranges=[4, 0, 0, 0, 4, 0, 0, 0, 4]) == 1
