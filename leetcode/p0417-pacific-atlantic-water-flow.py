#!/usr/bin/env python3

class Solution(object):
    from typing import List
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if len(matrix) == 0:
            return []
        if len(matrix) == 1:
            return [[0, i] for i in range(len(matrix[0]))]
        if len(matrix[0]) == 0:
            return []
        if len(matrix[0]) == 1:
            return [[i, 0] for i in range(len(matrix))]

        m = len(matrix)
        n = len(matrix[0])

        pacific_visit = []
        atlantic_visit = []
        for i in range(m):
            pacific_visit.append([0] * n)
            atlantic_visit.append([0] * n)

        for i in range(m):
            self.dfs(i, 0, m, n, matrix, pacific_visit)
            self.dfs(i, n-1, m, n, matrix, atlantic_visit)
        for j in range(n):
            self.dfs(0, j, m, n, matrix, pacific_visit)
            self.dfs(m-1, j, m, n, matrix, atlantic_visit)

        res = []
        for i in range(m):
            for j in range(n):
                if pacific_visit[i][j] == 1 and atlantic_visit[i][j] == 1:
                    res.append([i,j])

        return res

    def dfs(self, i: int, j: int, m: int, n: int, matrix: List[List[int]], visit: List[List[int]]):
        if i < 0 or i >= m or j < 0 or j >= n:
            return
        if visit[i][j] == 1:
            return
        visit[i][j] = 1
        if i + 1 < m and matrix[i][j] <= matrix[i+1][j]:
            self.dfs(i+1, j, m, n, matrix, visit)
        if i - 1 >= 0 and matrix[i][j] <= matrix[i-1][j]:
            self.dfs(i-1, j, m, n, matrix, visit)
        if j + 1 < n and matrix[i][j] <= matrix[i][j+1]:
            self.dfs(i, j+1, m, n, matrix, visit)
        if j - 1 >= 0 and matrix[i][j] <= matrix[i][j-1]:
            self.dfs(i, j-1, m, n, matrix, visit)

if __name__ == '__main__':
    res = Solution().pacificAtlantic([
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4]
    ])
    assert res == [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]

    # WA
    res2 = Solution().pacificAtlantic([
        [1, 2, 3],
        [8, 9, 4],
        [7, 6, 5]
    ])
    assert res2 == [[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]