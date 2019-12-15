#!/usr/bin/env python3

import math
import itertools
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
    def TLE_maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        """
        tried to simulate p1277
        """
        lendp = []

        m = len(mat)
        n = len(mat[0])

        for _ in range(m + 1):
            lendp.append([0] * (n + 1))

        res = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if mat[i - 1][j - 1] > threshold:
                    lendp[i][j] = 0
                else:
                    tmplen = min(lendp[i - 1][j], lendp[i][j - 1], lendp[i - 1][j - 1]) + 1
                    while True:
                        tmpsum = 0
                        for row in range(i - tmplen, i):
                            tmpsum += sum(mat[row][j - tmplen:j])
                            if tmpsum > threshold:
                                break
                        if tmpsum > threshold:
                            tmplen -= 1
                        else:
                            lendp[i][j] = tmplen
                            break
                    res = max(res, lendp[i][j])

        return res

    def TLE_2_maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        """
        refer to
        https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/discuss/451843/Java-PrefixSum-solution
        """
        dp = []

        m = len(mat)
        n = len(mat[0])

        for _ in range(m + 1):
            dp.append([0] * (n + 1))

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + mat[i - 1][j - 1]

        tmplen = min(m, n)
        while tmplen > 0:
            for i in range(1, (m + 1 - tmplen) + 1):
                for j in range(1, (n + 1 - tmplen) + 1):
                    if self.sub_matrix(i, j, i + tmplen - 1, j + tmplen - 1, dp) <= threshold:
                        return tmplen
            tmplen -= 1

        return 0

    def sub_matrix(self, i, j, x, y, dp: List[List[int]]) -> int:
        return dp[x][y] - dp[i - 1][y] - dp[x][j - 1] + dp[i - 1][j - 1]


    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        """
        refer to
        https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/discuss/451871/Java-sum%2Bbinary-O(m*n*log(min(mn)))
        """
        dp = []

        m = len(mat)
        n = len(mat[0])

        for _ in range(m + 1):
            dp.append([0] * (n + 1))

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + mat[i - 1][j - 1]

        lo = 0
        hi = min(m, n)
        while lo <= hi:
            tmplen = lo + (hi - lo) // 2
            if self.found(tmplen, m, n, dp, threshold):
                lo = tmplen + 1
            else:
                hi = tmplen - 1

        return hi

    def found(self, tmplen: int, m: int, n: int, dp: List[List[int]], threshold: int) -> bool:
        for i in range(1, (m + 1 - tmplen) + 1):
            for j in range(1, (n + 1 - tmplen) + 1):
                x = i + tmplen - 1
                y = j + tmplen - 1
                if dp[x][y] - dp[i - 1][y] - dp[x][j - 1] + dp[i - 1][j - 1] <= threshold:
                    return True
        return False


if __name__ == '__main__':
    assert Solution().maxSideLength(
        mat=[[1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2]],
        threshold=4
    ) == 2

    assert Solution().maxSideLength(
        mat=[[2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2]],
        threshold=1
    ) == 0

    assert Solution().maxSideLength(
        mat=[[1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]], threshold=6
    ) == 3

    assert Solution().maxSideLength(
        mat=[[18, 70], [61, 1], [25, 85], [14, 40], [11, 96], [97, 96], [63, 45]], threshold=40184
    ) == 2
