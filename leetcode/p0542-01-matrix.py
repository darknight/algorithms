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
    def TLE_updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        dfs is not for this type of question
        """
        m = len(matrix)
        assert m > 0
        n = len(matrix[0])
        assert n > 0

        MAX = m * n
        res = []
        visited = []
        for i in range(m):
            res.append([MAX] * n)
            visited.append([False] * n)
            for j in range(n):
                if matrix[i][j] == 0:
                    res[i][j] = 0
                    visited[i][j] = True

        def dfs(i, j, m, n) -> int:
            if i < 0 or i >= m or j < 0 or j >= n:
                return MAX
            elif visited[i][j] is True:
                return res[i][j]
            else:
                visited[i][j] = True
                up = dfs(i-1, j, m, n)
                down = dfs(i+1, j, m, n)
                left = dfs(i, j-1, m, n)
                right = dfs(i, j+1, m, n)
                res[i][j] = 1 + min(up, down, left, right)
                visited[i][j] = False
                return res[i][j]

        for i in range(m):
            for j in range(n):
                dfs(i, j, m, n)
                visited[i][j] = True

        # print(res)
        return res

    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        """bfs"""
        m = len(matrix)
        assert m > 0
        n = len(matrix[0])
        assert n > 0

        res = []
        queue = []
        for i in range(m):
            res.append([-1] * n)
            for j in range(n):
                if matrix[i][j] == 0:
                    res[i][j] = 0
                    queue.append((i, j))

        def update(i, j, dist, q):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if res[i][j] == -1:
                res[i][j] = dist
                q.append((i, j))

        dist = 1
        while len(queue) > 0:
            tmp = []
            while len(queue) > 0:
                i, j = queue.pop(0)
                update(i+1, j, dist, tmp)
                update(i-1, j, dist, tmp)
                update(i, j+1, dist, tmp)
                update(i, j-1, dist, tmp)
            queue = tmp
            dist += 1

        # print(res)
        return res


if __name__ == '__main__':
    # assert Solution().updateMatrix([[0,0,0],[0,1,0],[0,0,0]]) == [[0,0,0],[0,1,0],[0,0,0]]
    # assert Solution().updateMatrix([[0,0,0],[0,1,0],[1,1,1]]) == [[0,0,0],[0,1,0],[1,2,1]]
    assert Solution().updateMatrix([[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]])
    assert Solution().updateMatrix([[0,0,1,0,1,1,1,0,1,1],[1,1,1,1,0,1,1,1,1,1],[1,1,1,1,1,0,0,0,1,1],[1,0,1,0,1,1,1,0,1,1],[0,0,1,1,1,0,1,1,1,1],[1,0,1,1,1,1,1,1,1,1],[1,1,1,1,0,1,0,1,0,1],[0,1,0,0,0,1,0,0,1,1],[1,1,1,0,1,1,0,1,0,1],[1,0,1,1,1,0,1,1,1,0]])
