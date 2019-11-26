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

    def WA_countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visit = []
        for _ in range(m):
            visit.append([[0, 0]] * n)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and visit[i][j] != [1, 1]:
                    num = self.WA_bfs(i, j, m, n, grid, visit)
                    print(num)
                    if num > 1:
                        res += num
        return res

    def WA_bfs(self, i, j, m, n, grid, visit) -> int:
        queue = [(i, j)]
        connected = 0
        while len(queue) > 0:
            connected += 1
            row, col = queue.pop(0)
            for c in range(n):
                if c == col:
                    continue
                if visit[row][c] == [1, 1]:
                    break
                visit[row][c][0] += 1
                if grid[row][c] == 1:
                    queue.append((row, c))

            for r in range(m):
                if r == row:
                    continue
                if visit[r][col] == [1, 1]:
                    break
                visit[r][col][1] += 1
                if grid[r][col] == 1:
                    queue.append((r, col))

            visit[row][col] = [1, 1]

        return connected

    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visit_row = [0] * m
        visit_col = [0] * n

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and visit_row[i] == 0 and visit_col[j] == 0:
                    num = self.bfs(i, j, m, n, grid, visit_row, visit_col)
                    if num > 1:
                        res += num
        return res

    def bfs(self, i, j, m, n, grid, visit_row, visit_col) -> int:
        queue = [(i, j)]
        connected = 0
        while len(queue) > 0:
            connected += 1
            row, col = queue.pop(0)
            if visit_row[row] == 0:
                visit_row[row] = 1
                for c in range(n):
                    if c == col:
                        continue
                    if grid[row][c] == 1 and visit_col[c] == 0:
                        queue.append((row, c))

            if visit_col[col] == 0:
                visit_col[col] = 1
                for r in range(m):
                    if r == row:
                        continue
                    if grid[r][col] == 1 and visit_row[r] == 0:
                        queue.append((r, col))

        return connected

if __name__ == '__main__':
    assert Solution().countServers([[1,0],[0,1]]) == 0
    assert Solution().countServers([[1, 0], [1, 1]]) == 3
    assert Solution().countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]) == 4

    assert Solution().countServers([[0,0,0,0],[1,1,1,1],[0,0,0,1],[0,0,1,1],[0,0,0,1]]) == 8
