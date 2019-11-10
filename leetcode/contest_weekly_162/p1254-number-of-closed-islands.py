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
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        marked = []
        for _ in range(m):
            marked.append([0] * n)

        for j in range(n):
            if grid[0][j] == 0:
                self.bfs(0, j, m, n, grid, marked, 2)
            if grid[m - 1][j] == 0:
                self.bfs(m - 1, j, m, n, grid, marked, 2)

        for i in range(1, m - 1):
            if grid[i][0] == 0:
                self.bfs(i, 0, m, n, grid, marked, 2)
            if grid[i][n - 1] == 0:
                self.bfs(i, n - 1, m, n, grid, marked, 2)

        res = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0:
                    self.bfs(i, j, m, n, grid, marked, 3)
                    res += 1

        return res

    def bfs(self, i: int, j: int, m: int, n: int, grid: List[List[int]], marked: List[List[int]], status: int):
        # invalid
        if i < 0 or i >= m or j < 0 or j >= n:
            return
        # visited or water
        if marked[i][j] == 1 or grid[i][j] == 1:
            return
        grid[i][j] = status
        marked[i][j] = 1

        self.bfs(i - 1, j, m, n, grid, marked, status)
        self.bfs(i + 1, j, m, n, grid, marked, status)
        self.bfs(i, j - 1, m, n, grid, marked, status)
        self.bfs(i, j + 1, m, n, grid, marked, status)


if __name__ == '__main__':
    assert Solution().closedIsland([[1, 1, 1, 1, 1, 1, 1, 0],
                                    [1, 0, 0, 0, 0, 1, 1, 0],
                                    [1, 0, 1, 0, 1, 1, 1, 0],
                                    [1, 0, 0, 0, 0, 1, 0, 1],
                                    [1, 1, 1, 1, 1, 1, 1, 0]]) == 2
    assert Solution().closedIsland([[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]) == 1
    assert Solution().closedIsland([[1, 1, 1, 1, 1, 1, 1],
                                    [1, 0, 0, 0, 0, 0, 1],
                                    [1, 0, 1, 1, 1, 0, 1],
                                    [1, 0, 1, 0, 1, 0, 1],
                                    [1, 0, 1, 1, 1, 0, 1],
                                    [1, 0, 0, 0, 0, 0, 1],
                                    [1, 1, 1, 1, 1, 1, 1]]) == 2
