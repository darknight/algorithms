#!/usr/bin/env python3

class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def _minPathSum(self, grid):
        '''
        Time Limit Exceeded
        '''
        def pathSum(i, j):
            if i == 0 and j == 0:
                return grid[0][0]
            elif i == 0:
                return sum(grid[0][:j+1])
            elif j == 0:
                res = 0
                for row in range(i+1):
                    res += grid[row][0]
                return res
            s1 = pathSum(i-1, j)
            s2 = pathSum(i, j-1)
            return min(s1, s2) + grid[i][j]

        if len(grid) == 0:
            return 0
        i = len(grid) - 1
        j = len(grid[0]) - 1
        return pathSum(i, j)

    def minPathSum(self, grid):
        '''
        recursive formula:
        sum(i,j) = min(sum(i-1,j), sum(i,j-1)) + grid(i,j)
        '''
        if len(grid) == 0:
            return 0
        if len(grid) > 0 and len(grid[0]) == 0:
            return 0
        row = len(grid)
        column = len(grid[0])
        cache = [[-1] * column for _ in range(row)]
        for i in range(row):
            cache[i][0] = grid[i][0]
        for i in range(1, row):
            cache[i][0] += cache[i-1][0]
        for j in range(column):
            cache[0][j] = grid[0][j]
        for j in range(1, column):
            cache[0][j] += cache[0][j-1]
        #for j in range(column):
        #    cache[0][j] = sum(grid[0][:j+1])

        def pathSum(i, j):
            if i == 0 or j == 0 or cache[i][j] >= 0:
                return cache[i][j]
            s1 = pathSum(i-1, j)
            s2 = pathSum(i, j-1)
            cache[i][j] = min(s1, s2) + grid[i][j]
            return cache[i][j]

        return pathSum(row-1, column-1)

if __name__ == '__main__':
    grid1 = [
        [1,2,3,4],
        [4,3,2,1],
        [5,3,7,1],
        [9,3,1,7]
            ]
    grid2 = [[3]]
    grid3 = []
    grid4 = [[1,2,3]]
    grid5 = [[1],[2],[3]]
    print(Solution().minPathSum(grid1))
    print(Solution().minPathSum(grid2))
    print(Solution().minPathSum(grid3))
    print(Solution().minPathSum(grid4))
    print(Solution().minPathSum(grid5))

    case = [[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]
    print(Solution().minPathSum(case))

