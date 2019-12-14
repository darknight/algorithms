#!/usr/bin/env python3

import math
from collections import defaultdict
from typing import List
from typing import Set

try:
    from _tree import *
except ImportError:
    pass

try:
    from _uitl import *
except ImportError:
    pass


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        """
        refer to
        https://leetcode.com/problems/count-square-submatrices-with-all-ones/discuss/441620/DP-with-figure-explanation
        https://leetcode.com/problems/count-square-submatrices-with-all-ones/discuss/441431/Python-DP-Solution-with-Explaination
        """
        m = len(matrix)
        n = len(matrix[0])

        res = 0
        dp = []
        for _ in range(m + 1):
            dp.append([0] * (n + 1))

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == 1:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                else:
                    dp[i][j] = 0
                res += dp[i][j]

        return res


if __name__ == '__main__':
    pass
