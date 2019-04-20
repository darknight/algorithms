#!/usr/bin/env python3

class Solution:
    # @param matrix, a list of lists of integers
    # @return nothing (void), do not return anything, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        rows = []
        cols = []
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])
        if m == 1 and n <= 1:
            return
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i not in rows:
                        rows.append(i)
                    if j not in cols:
                        cols.append(j)
        for row in rows:
            for j in range(n):
                matrix[row][j] = 0
        for col in cols:
            for i in range(m):
                matrix[i][col] = 0

if __name__ == '__main__':
    Solution().setZeroes([[0]])
    Solution().setZeroes([[1]])
    Solution().setZeroes([[0,1]]) # WA for this case
    Solution().setZeroes([[1,0]])
    Solution().setZeroes([[1,2],[3,0]])
    Solution().setZeroes([[1,2,3],[4,0,6],[7,8,9]])
    Solution().setZeroes([[1,0,3,4],[5,6,7,8]])

