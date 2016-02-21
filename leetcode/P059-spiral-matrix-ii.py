class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        if n == 1:
            return [[1]]
        res = []
        for i in range(n):
            res.append([0]*n)

        row = -1
        col = -1
        k = 1
        while n > 0:
            row += 1
            col += 1
            # first row
            i = row
            for j in range(n):
                if res[i][col+j] == 0:
                    res[i][col+j] = k
                    k += 1
            # last column
            j = col + n - 1
            for i in range(n):
                if res[row+i][j] == 0:
                    res[row+i][j] = k
                    k += 1
            # last row
            i = row + n - 1
            for j in range(n):
                if res[i][col+n-1-j] == 0:
                    res[i][col+n-1-j] = k
                    k += 1
            # first column
            j = col
            for i in range(n):
                if res[row+n-1-i][j] == 0:
                    res[row+n-1-i][j] = k
                    k += 1

            n -= 2

        return res

if __name__ == '__main__':
    for n in range(2, 7):
        matrix = Solution().generateMatrix(n)
        for i in range(n):
            print matrix[i]
