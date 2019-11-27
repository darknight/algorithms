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
    def AC_maxSumDivThree(self, nums: List[int]) -> int:
        res = [0]
        total = sum(nums)
        self.dfs(0, total, nums, res)
        return res[-1]

    def dfs(self, i: int, total: int, nums: List[int], res: List[int]):
        if i >= len(nums):
            return
        # take
        if total % 3 == 0:
            res[-1] = total
        self.dfs(i + 1, total, nums, res)
        # not take
        tmp = total - nums[i]
        if tmp % 3 == 0 and tmp > res[-1]:
            res[-1] = tmp
        # truncate
        if res[-1] > tmp:
            return
        self.dfs(i + 1, tmp, nums, res)

    # FIXME: very slow, why?
    def maxSumDivThree(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/greatest-sum-divisible-by-three/discuss/431088/C%2B%2B-dp-solution
        f[i][j] denotes the maximum subset sum select from nums[0] - nums[i] which modulos 3 equal to j
        reutrn f[-1][0]

        hint:
        Represent the state as DP[pos][mod]: maximum possible sum starting in the position "pos"
        in the array where the current sum modulo 3 is equal to mod.
        """
        nums.insert(0, 0)
        size = len(nums)
        dp = [[0] * 3 for _ in range(size)]
        for i in range(1, size):
            for j in range(3):
                jj = (j + 3 - nums[i] % 3) % 3
                choose = dp[i - 1][jj] + nums[i]
                if choose % 3 == j:
                    dp[i][j] = max(dp[i - 1][j], choose)
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][0]



if __name__ == '__main__':
    assert Solution().maxSumDivThree([3, 6, 5, 1, 8]) == 18
    # assert Solution().maxSumDivThree([4]) == 0
    # assert Solution().maxSumDivThree([1, 2, 3, 4, 4]) == 12
