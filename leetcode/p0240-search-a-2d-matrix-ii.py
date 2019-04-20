#!/usr/bin/env python3

class Solution(object):
    def _searchMatrix(self, matrix, target):
        """
        Time Limit Exceeded
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False

        tmp = [[0] * n for _ in range(m)]
        res = [False]
        def _dfs(i, j):
            if i < m and j < n and not res[0] and not tmp[i][j]:
                if matrix[i][j] == target:
                    res[0] = True
                    return
                if matrix[i][j] > target:
                    return
                tmp[i][j] = 1
                _dfs(i+1, j)
                _dfs(i, j+1)
        _dfs(0, 0)
        return res[0]

    def __searchMatrix(self, matrix, target):
        """
        Time Limit Exceeded
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False

        i = 0
        j = 0
        while i < m and j < n:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                break
            i += 1
            j += 1

        tmp = [[0] * n for _ in range(m)]
        res = [False]
        def _dfs(i, j, m, n):
            if i < m and j < n and not res[0] and not tmp[i][j]:
                if matrix[i][j] == target:
                    res[0] = True
                    return
                if matrix[i][j] > target:
                    return
                tmp[i][j] = 1
                _dfs(i+1, j, m, n)
                _dfs(i, j+1, m, n)

        if i >= m:
            _dfs(0, j, m, n)
        elif j >= n:
            _dfs(i, 0, m, n)
        else:
            _dfs(i, 0, m, j)
            _dfs(0, j, i, n)
        return res[0]

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False

        res = [False]
        def _dc(row, col, m, n):
            if res[0] is True:
                return
            if row >= m or col >= n:
                return
            i = row
            j = col
            while i < m and j < n:
                if matrix[i][j] == target:
                    res[0] = True
                    return
                if matrix[i][j] > target:
                    break
                i += 1
                j += 1
            _dc(i, col, m, j)
            _dc(row, j, i, n)

        _dc(0, 0, m, n)
        return res[0]

if __name__ == '__main__':
    print(Solution().searchMatrix([[-1, 3]], 3) == True)
    print(Solution().searchMatrix([[-5]], -2) == False)
    matrix = [
        [1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25],
    ]
    print(Solution().searchMatrix(matrix, 15) == True)
    matrix = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    print(Solution().searchMatrix(matrix, 5) == True)
    print(Solution().searchMatrix(matrix, 8) == True)
    print(Solution().searchMatrix(matrix, 20) == False)
    matrix = [
        [5,9,11,12,14,17,20,22],
        [6,13,17,22,25,27,27,32],
        [9,15,22,26,28,31,35,39],
        [13,16,24,30,30,33,35,44],
        [16,19,28,34,39,44,47,47],
        [18,20,30,39,43,48,49,53],
        [22,25,32,40,48,52,56,59],
        [25,26,35,44,52,57,58,63],
        [25,31,36,47,52,60,60,63],
        [25,36,37,52,52,62,63,68],
    ]
    print(Solution().searchMatrix(matrix, 45) == False)
