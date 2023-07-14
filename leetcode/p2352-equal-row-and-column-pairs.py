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
    def equalPairs(self, grid: List[List[int]]) -> int:
        N = len(grid)
        rows = grid
        cols = []
        for j in range(N):
            col = []
            for i in range(N):
                col.append(grid[i][j])
            cols.append(col)

        res = 0
        for i in range(N):
            for j in range(N):
                if rows[i] == cols[j]:
                    res += 1

        return res


if __name__ == '__main__':
    pass
