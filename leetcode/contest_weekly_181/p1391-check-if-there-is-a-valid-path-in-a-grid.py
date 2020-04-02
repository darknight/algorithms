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
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        M = len(grid)
        N = len(grid[0])
        res = [False]
        visit = [[0] * N for _ in range(M)]

        def dfs(row: int, col: int, expect: List[int]):
            if row < 0 or row >= M:
                return
            if col < 0 or col >= N:
                return
            if grid[row][col] not in expect:
                return
            if row == M - 1 and col == N - 1:
                res[0] = True
                return
            if visit[row][col] == 1:
                return

            visit[row][col] = 1
            street = grid[row][col]
            if street == 1:
                dfs(row, col + 1, [1, 3, 5])
                dfs(row, col - 1, [1, 4, 6])
            elif street == 2:
                dfs(row + 1, col, [2, 5, 6])
                dfs(row - 1, col, [2, 3, 4])
            elif street == 3:
                dfs(row + 1, col, [2, 5, 6])
                dfs(row, col - 1, [1, 4, 6])
            elif street == 4:
                dfs(row + 1, col, [2, 5, 6])
                dfs(row, col + 1, [1, 3, 5])
            elif street == 5:
                dfs(row - 1, col, [2, 3, 4])
                dfs(row, col - 1, [1, 4, 6])
            else:
                dfs(row - 1, col, [2, 3, 4])
                dfs(row, col + 1, [1, 3, 5])

        dfs(0, 0, [1, 2, 3, 4, 6])
        return res[0]


if __name__ == '__main__':
    # assert Solution().hasValidPath(grid = [[1,1,1,1,1,1,3]]) is True
    assert Solution().hasValidPath([[4,1],[6,1]]) is True
