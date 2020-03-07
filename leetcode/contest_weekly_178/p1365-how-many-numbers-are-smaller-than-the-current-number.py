#!/usr/bin/env python3

import math, itertools, functools, heapq
from collections import defaultdict, Counter
from typing import List, Set, Dict, Tuple
try:
    from _tree import *
    from _list import *
    from _util import *
except ImportError:
    pass


class Solution:
    def AC_smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for i in range(len(nums)):
            cnt = 0
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[j] < nums[i]:
                    cnt += 1
            res[i] = cnt

        return res

    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """
        refer to
        https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/discuss/525062/Python-Extremely-Simple-Solution
        """
        snums = sorted(nums)
        res = [snums.index(n) for n in nums]
        return res


if __name__ == '__main__':
    pass
