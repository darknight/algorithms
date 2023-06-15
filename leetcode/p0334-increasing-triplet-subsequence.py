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
    def increasingTriplet_TLE(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        for i in range(n-2):
            for j in range(i+1, n-1):
                if nums[i] >= nums[j]:
                    continue
                for k in range(j+1, n):
                    if nums[j] < nums[k]:
                        return True
        return False

    def increasingTriplet_official(self, nums: List[int]) -> bool:
        """
        nums = [1,2,0,3] # should return True
        first_num = 1
        second_num = 2
        first_num = 0
        return True

        Observation: there exists another number before second_num(2) which is
        definitely BIGGER than the last updated first_num(0) but SMALLER than second_num
        """
        first = math.inf
        second = math.inf
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False


if __name__ == '__main__':
    pass
