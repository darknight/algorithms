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
    def longestOnes_WA_TLE(self, nums: List[int], k: int) -> int:
        """
        sliding window
        """
        size = len(nums)
        res = 0
        for left in range(size):
            flip = k
            if nums[left] == 0:
                if flip > 0:
                    flip -= 1
                else:
                    continue
            right = left + 1
            while right < size:
                if nums[right] == 1:
                    right += 1
                    continue
                elif flip > 0:
                    flip -= 1
                    right += 1
                    continue
                else:
                    break
            res = max(res, right - left)

        return res

    def longestOnes_official(self, nums: List[int], k: int) -> int:
        """
        Since we have to find the MAXIMUM window, we never reduce the size of the window.
        """
        size = len(nums)
        left = right = 0
        for right in range(size):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1

        return right - left + 1

    def longestOnes_other(self, nums: List[int], k: int) -> int:
        """
        shrink window, easy understanding
        https://leetcode.com/problems/max-consecutive-ones-iii/solutions/692111/simple-c-explanation-for-easy-understanding-o-n-time-and-o-1-space/
        """
        res = 0
        zeros = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            res = max(res, right-left+1)

        return res


if __name__ == '__main__':
    pass
