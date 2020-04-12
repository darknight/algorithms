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
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        total = sum(nums)

        for i in range(len(nums)):
            s = sum(nums[:i+1])
            if s > total - s:
                return nums[:i+1]

        return []



if __name__ == '__main__':
    pass
