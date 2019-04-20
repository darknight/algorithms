#!/usr/bin/env python3

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        if n == 0:
            return 0
        if m == 1 and n == 1:
            if obstacleGrid[0][0] == 0:
                return 1
            return 0
        cache = [[0]*n for _ in range(m)]
        cache[0][0] = 1-obstacleGrid[0][0]
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                cache[i][0] = 0
            else:
                cache[i][0] = cache[i-1][0]
        for j in range(1, n):
            if obstacleGrid[0][j] == 1:
                cache[0][j] = 0
            else:
                cache[0][j] = cache[0][j-1]
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    cache[i][j] = 0
                else:
                    cache[i][j] = cache[i-1][j] + cache[i][j-1]
        return cache[m-1][n-1]

if __name__ == '__main__':
    grid = [
        [0,1,0],
        [1,0,0],
        [0,0,0],
    ]
    #print(Solution().uniquePathsWithObstacles(grid))
    print(Solution().uniquePathsWithObstacles([[1,0]]))
