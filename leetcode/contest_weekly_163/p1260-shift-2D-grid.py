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
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if k == 0:
            return grid

        m = len(grid)
        n = len(grid[0])
        new_grid = []
        for _ in range(m):
            new_grid.append([0] * n)

        for i in range(m):
            for j in range(n):
                new_j = (j + k) % n
                new_i = (i + (j + k) // n) % m
                new_grid[new_i][new_j] = grid[i][j]

        print(new_grid)
        return new_grid




if __name__ == '__main__':
    Solution().shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1)
    Solution().shiftGrid(grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4)
    Solution().shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9)
