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
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums) - nums[0]
        pivot = 0
        while left != right and pivot < len(nums) - 1:
            left += nums[pivot]
            pivot += 1
            right -= nums[pivot]

        if left == right:
            return pivot
        return -1



if __name__ == '__main__':
    pass
