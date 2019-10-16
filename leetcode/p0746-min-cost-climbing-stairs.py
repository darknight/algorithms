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
    def AC_minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        f(i) = min(f(i-1)+a[i], f(i-2)+a[i-2])
        f(0) = 0
        f(1) = 0
        """
        size = len(cost)
        if size < 2:
            return 0

        cost.append(0)
        res = [0] * (size + 1)
        for i in range(2, size+1):
            res[i] = min(res[i-1]+cost[i-1], res[i-2]+cost[i-2])

        return res[-1]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        f(i) = min(f(i-1)+a[i], f(i-2)+a[i-2])
        f(0) = 0
        f(1) = 0
        """
        size = len(cost)
        if size < 2:
            return 0

        cost.append(0)
        prev2 = 0
        prev1 = 0
        for i in range(2, size+1):
            curr = min(prev1+cost[i-1], prev2+cost[i-2])
            prev2 = prev1
            prev1 = curr

        return prev1


if __name__ == '__main__':
    assert Solution().minCostClimbingStairs([10, 15, 20]) == 15
    assert Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
