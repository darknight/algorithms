#!/usr/bin/env python3

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        #TODO: slow & improve
        m = len(matrix)
        if m == 0:
            return []
        if m == 1:
            return matrix[0]
        n = len(matrix[0])
        if n == 0:
            return []
        res = []
        if n == 1:
            for i in range(m):
                res.append(matrix[i][0])
            return res

        row = -1
        col = -1
        while m > 0 and n > 0:
            row += 1
            col += 1
            # first row
            i = row
            for j in range(n):
                res.append(matrix[i][col+j])
            # last column
            j = col + n - 1
            for i in range(1, m):
                res.append(matrix[row+i][j])
            # last row
            if m != 1:
                i = row + m - 1
                for j in range(1, n):
                    res.append(matrix[i][col+n-1-j])
            if n != 1:
                # first column
                j = col
                for i in range(1, m-1):
                    res.append(matrix[row+m-1-i][j])
            m -= 2
            n -= 2

        return res

if __name__ == '__main__':
    matrix = [
       [ 1, 2, 3],
       [ 4, 5, 6],
       [ 7, 8, 9],
       [ 12, 11, 10],
    ]
    print(Solution().spiralOrder(matrix))
