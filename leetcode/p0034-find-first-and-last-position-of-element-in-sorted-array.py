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
    def searchRange_2_passes(self, nums: List[int], target: int) -> List[int]:
        error = [-1, -1]
        length = len(nums)
        if length == 0:
            return error
        if length == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return error
        i = 0
        j = length - 1
        lower = -1
        upper = -1
        while i <= j and i < length and j >= 0:
            mid = (i + j) // 2
            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] > target:
                j = mid - 1
            else:
                if nums[i] < target:
                    i += 1
                else:
                    lower = i
                    break

        i = 0
        j = length - 1
        while i <= j and i < length and j >= 0:
            mid = (i + j) // 2
            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] > target:
                j = mid - 1
            else:
                if nums[j] > target:
                    j -= 1
                else:
                    upper = j
                    break
        if lower == -1 or upper == -1:
            return error
        return [lower, upper]

    def searchRange_old(self, nums: List[int], target: int) -> List[int]:

        def binary_search(nums: List[int], target: int) -> int:
            l = 0
            h = len(nums)  # from 3rd party
            while l < h:
                m = l + (h - l) // 2
                if nums[m] >= target:
                    h = m
                else:
                    l = m + 1
            return l

        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1,-1]
        low = binary_search(nums, target)
        if low >= len(nums) or nums[low] != target:
            return [-1, -1]
        high = binary_search(nums, target+1)
        return [low, high-1]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        def search_low(nums: List[int], target: int) -> int:
            i = 0
            j = len(nums) - 1
            left = -1
            while i <= j:
                mid = (i + j) // 2
                if nums[mid] < target:
                    i = mid + 1
                elif nums[mid] > target:
                    j = mid - 1
                else:
                    left = mid
                    j = mid - 1
            return left

        def search_high(nums: List[int], target: int) -> int:
            i = 0
            j = len(nums) - 1
            right = -1
            while i <= j:
                mid = (i + j) // 2
                if nums[mid] < target:
                    i = mid + 1
                elif nums[mid] > target:
                    j = mid - 1
                else:
                    right = mid
                    i = mid + 1
            return right

        low = search_low(nums, target)
        if low == -1:
            return [-1, -1]
        return [low, search_high(nums, target)]


if __name__ == '__main__':
    assert Solution().searchRange([1,2,3,4,5,7,7,8,9,10], 8) == [7,7]
    assert Solution().searchRange([5,7,7,8,8,10], 8) == [3,4]
    assert Solution().searchRange([5,7,7,8,8,10], 6) == [-1,-1]
    assert Solution().searchRange([2,2], 2) == [0,1]

