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
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        """
        checked answer

        just a simple dfs, the data limit is quite small, so iterate all vertex is possible
        """

        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0

        grid.insert(0, [0] * (n + 2))
        grid.append([0] * (n + 2))
        for i in range(1, m+1):
            grid[i].insert(0, 0)
            grid[i].append(0)

        visit = []
        for _ in range(m+2):
            visit.append([0] * (n+2))

        def dfs(i, j, curr: int, res: List[int]):
            if visit[i][j] == 1:
                return
            if grid[i][j] == 0:
                res[0] = max(res[0], curr)
                return
            visit[i][j] = 1
            dfs(i + 1, j, curr + grid[i][j], res)
            dfs(i - 1, j, curr + grid[i][j], res)
            dfs(i, j + 1, curr + grid[i][j], res)
            dfs(i, j - 1, curr + grid[i][j], res)
            visit[i][j] = 0

        # print(grid)
        # print(visit)
        res = [0]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if grid[i][j] > 0:
                    dfs(i, j, 0, res)

        # print(res)
        return res[0]


if __name__ == '__main__':
    assert Solution().getMaximumGold([[0,6,0],[5,8,7],[0,9,0]]) == 24
    assert Solution().getMaximumGold([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]) == 28
