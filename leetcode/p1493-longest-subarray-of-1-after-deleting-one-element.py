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
    def longestSubarray(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 1:
            return 0
        i = 0
        zeros = 0
        res = 0
        for j in range(size):
            if nums[j] == 1:
                print(i, j, zeros)
                res = max(res, j-i+1-zeros)
            elif zeros == 0:
                zeros = 1
                continue
            else:
                while nums[i] != 0:
                    i += 1
                i += 1
        if zeros == 0 and res > 0:
            res -= 1

        return res

    def longestSubarray_official(self, nums: List[int]) -> int:
        zero_count = 0
        res = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            res = max(res, right - left)

        return res


if __name__ == '__main__':
    print(Solution().longestSubarray([0,1,1,1,0,1,1,0,1]))
