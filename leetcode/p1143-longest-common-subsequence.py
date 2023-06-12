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
    def longestCommonSubsequence_official_top_down(self, text1: str, text2: str) -> int:
        @lru_cache(maxsize=None)
        def solve(p1: int, p2: int) -> int:
            if p1 == len(text1) or p2 ==  len(text2):
                return 0

            # text1[p1] is not part of optimal solution
            case1 = solve(p1+1, p2)

            # text1[p] is part of optimal solution
            case2 = 0
            first_occurence = text2.find(text1[p1], p2)
            if first_occurence != -1:
                case2 = 1 + solve(p1+1, first_occurence+1)

            return max(case1, case2)

        return solve(0, 0)

    def longestCommonSubsequence_official_top_down_v2(self, text1: str, text2: str) -> int:
        @lru_cache(maxsize=None)
        def solve(p1: int, p2: int) -> int:
            if p1 == len(text1) or p2 ==  len(text2):
                return 0

            if text1[p1] == text2[p2]:
                return 1 + solve(p1+1, p2+1)
            else:
                return max(solve(p1, p2+1), solve(p1+1, p2))

        return solve(0, 0)

    def longestCommonSubsequence_official_bottom_up(self, text1: str, text2: str) -> int:
        grid = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]

        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                if text2[col] == text1[row]:
                    grid[row][col] = 1 + grid[row+1][col+1]
                else:
                    grid[row][col] = max(grid[row+1][col], grid[row][col+1])

        return grid[0][0]


if __name__ == '__main__':
    pass
