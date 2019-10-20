#!/usr/bin/env python3

import math
from collections import defaultdict
from typing import List
from typing import Set

try:
    from _tree import *
except ImportError:
    pass


class Solution:
    def TLE_probabilityOfHeads(self, prob: List[float], target: int) -> float:
        res = 1.0
        if target == 0:
            for p in prob:
                res = res * (1 - p)
            return res

        if target == len(prob):
            for p in prob:
                res = res * p
            return res

        size = len(prob)

        res = []

        def permutation(arr, i, n, tmp):
            if n == target:
                for k in range(i, size):
                    tmp = tmp * (1 - arr[k])
                res.append(tmp)
                return
            if i >= size:
                return
            permutation(arr, i + 1, n + 1, tmp * arr[i])
            permutation(arr, i + 1, n, tmp * (1 - arr[i]))

        permutation(prob, 0, 0, 1.0)

        # print(res, sum(res))
        return sum(res)

    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        """
        DP
        f(i, k) = f(i-1, k)*(1-a[i]) + f(i-1, k-1)*a[i]
        f(0, 0) = 1
        """
        size = len(prob)
        dp = []
        for i in range(size + 1):
            dp.append([0.0] * (target + 1))

        dp[0][0] = 1.0

        for i in range(1, size + 1):
            for t in range(target + 1):
                if t == 0:
                    dp[i][0] = dp[i - 1][0] * (1 - prob[i - 1])
                else:
                    dp[i][t] = dp[i - 1][t] * (1 - prob[i - 1]) + dp[i - 1][t - 1] * prob[i - 1]

        # print(dp)
        return dp[size][target]


if __name__ == '__main__':
    # assert Solution().probabilityOfHeads([0.4], 1) == 0.4
    # assert Solution().probabilityOfHeads([0.5,0.5,0.5,0.5,0.5], 0) == 0.03125
    assert Solution().probabilityOfHeads([0.1, 0.2, 0.3], 2) == 0.092
    # assert Solution().TLE_probabilityOfHeads([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 99) == 1
