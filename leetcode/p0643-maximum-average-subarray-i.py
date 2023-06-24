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
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = curr = sum(nums[:k]) / k
        size = len(nums)
        i = 0
        j = k
        while j < size:
            curr = curr - nums[i] / k + nums[j] / k
            res = max(res, curr)
            i += 1
            j += 1

        return res


if __name__ == '__main__':
    print(Solution().findMaxAverage([0,4,0,3,2], 1))
