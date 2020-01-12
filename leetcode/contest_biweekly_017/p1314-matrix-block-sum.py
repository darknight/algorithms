#!/usr/bin/env python3

import math, itertools
from collections import defaultdict, Counter
from typing import List, Set
try:
    from _tree import *
    from _list import *
    from _util import *
except ImportError:
    pass

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        dp = []
        for _ in range(m+1):
            dp.append([0] * (n+1))

        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + mat[i-1][j-1]

        res = []
        for _ in range(m):
            res.append([0] * n)

        for i in range(m):
            for j in range(n):
                r1, c1 = max(i-K, 0), max(j-K, 0)
                r2, c2 = min(i+K, m-1), min(j+K, n-1)
                res[i][j] = dp[r2+1][c2+1] - dp[r1][c2+1] - dp[r2+1][c1] + dp[r1][c1]

        return res

if __name__ == '__main__':
    Solution().matrixBlockSum(mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1)
    Solution().matrixBlockSum(mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2)
