class Solution:
    # @return an integer
    def _uniquePaths(self, m, n):
        '''
        Time Limit Exceeded
        '''
        if m == 0 or n == 0:
            return 0
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)

    def uniquePaths(self, m, n):
        '''
        N(i, j) = N(i-1, j) + N(i, j-1)
        N(0, j) = 1
        N(i, 0) = 1
        '''
        cache = [[0] * n for _ in range(m)]
        for i in range(m):
            cache[i][0] = 1
        for j in range(n):
            cache[0][j] = 1

        def path(row, col):
            if row >= 0  and col >=0:
                if cache[row][col] > 0:
                    return cache[row][col]
                else:
                    res = path(row-1, col) + path(row, col-1)
                    cache[row][col] = res
                    return res
            return 0

        return path(m-1, n-1)

if __name__ == '__main__':
    print Solution().uniquePaths(1, 1) == 1
    print Solution().uniquePaths(1, 5)
    print Solution().uniquePaths(2, 2)
    print Solution().uniquePaths(3, 3)
    print Solution().uniquePaths(2, 3)
    print Solution().uniquePaths(23, 12)
