#!/usr/bin/env python3

class Solution(object):
    from typing import List
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            row = grid[i]
            for j in range(len(row)):
                if grid[i][j] == 1:
                    area = self.dfs(i, j, grid)
                    res = max(res, area)

        return res

    def dfs(self, i: int, j: int, grid: List[List[int]]) -> int:
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
            return 0
        if grid[i][j] != 1:
            return 0
        grid[i][j] = 2
        return 1 + \
               self.dfs(i-1, j, grid) + self.dfs(i+1, j, grid) + \
               self.dfs(i, j-1, grid) + self.dfs(i, j+1, grid)

if __name__ == '__main__':
    assert Solution().maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]) == 6