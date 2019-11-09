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
    def TLE_numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """
        i is 0 -> size
        j is i -> size
        so O(N^2), definitely timeout...
        """
        size = len(nums)

        res = 0
        for i in range(size):
            res += self.f(i, k, size, nums)

        return res

    def f(self, i, K, size, nums: List[int]) -> int:
        res = 0
        oddcnt = 0
        for j in range(i, size):
            if nums[j] % 2 == 1:
                oddcnt += 1
            if oddcnt == K:
                res += 1

        return res

    # it's not DP...
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        size = len(nums)

        queue = []
        dp = [0] * size

        i = 0
        while len(queue) != k and i < size:
            if nums[i] % 2 == 1:
                queue.append(i)
            i += 1

        if len(queue) != k:
            return 0

        dp[i-1] = queue[0] - (-1)

        for j in range(i, size):
            if nums[j] % 2 == 1:
                prev = queue.pop(0)
                queue.append(j)
                dp[j] = queue[0] - prev
            else:
                dp[j] = dp[j-1]

        return sum(dp)


if __name__ == '__main__':
    # assert Solution().numberOfSubarrays([1,1,2,1,1], 3) == 2
    # assert Solution().numberOfSubarrays([2,4,6], 1) == 0
    assert Solution().numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2) == 16
