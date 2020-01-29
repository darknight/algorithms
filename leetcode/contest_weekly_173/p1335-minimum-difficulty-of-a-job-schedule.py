#!/usr/bin/env python3

import math, itertools, functools
from collections import defaultdict, Counter
from typing import List, Set, Dict, Tuple

try:
    from _tree import *
    from _list import *
    from _util import *
except ImportError:
    pass


class Solution:
    def TLE_minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        res = [math.inf]

        def dfs(prev_job, curr_d, curr_cost, size):
            if curr_d >= d:
                if prev_job < size - 1:
                    return
                else:
                    res[0] = min(res[0], curr_cost)
            else:
                if prev_job >= size - 1:
                    return
            curr_job = prev_job + 1
            for stop in range(curr_job, size):
                cost = max(jobDifficulty[curr_job:stop + 1])
                dfs(stop, curr_d + 1, curr_cost + cost, size)

        size = len(jobDifficulty)
        if size < d:
            return -1
        dfs(-1, 0, 0, size)

        return res[0]

    def DFS_minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        """
        refer to
        https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/discuss/490316/JavaC%2B%2BPython-DP
        """
        size = len(jobDifficulty)
        if size < d:
            return -1

        # the ith job, and days left
        @functools.lru_cache(maxsize=None)
        def dfs(left_d: int, curr_job: int) -> int:
            if left_d == 1:
                return max(jobDifficulty[curr_job:])
            res = math.inf
            max_cost = 0
            for j in range(curr_job, size - left_d + 1):
                max_cost = max(max_cost, jobDifficulty[j])
                res = min(res, max_cost + dfs(left_d - 1, j + 1))

            return res

        return dfs(d, 0)


if __name__ == '__main__':
    assert Solution().minDifficulty([6, 5, 4, 3, 2, 1], d=2) == 7
    assert Solution().minDifficulty([9, 9, 9], d=4) == -1
    assert Solution().minDifficulty([1, 1, 1], d=3) == 3
    assert Solution().minDifficulty([7, 1, 7, 1, 7, 1], d=3) == 15
    assert Solution().minDifficulty([11, 111, 22, 222, 33, 333, 44, 444], d=6) == 843
