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
    # O(N)
    def AC_findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        M = len(nums1)
        N = len(nums2)
        nums = []
        i = 0
        j = 0
        while i < M and j < N:
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
                continue
            if nums1[i] > nums2[j]:
                nums.append(nums2[j])
                j += 1
                continue
            nums.append(nums1[i])
            nums.append(nums2[j])
            i += 1
            j += 1
        while i < M:
            nums.append(nums1[i])
            i += 1
        while j < N:
            nums.append(nums2[j])
            j += 1

        L = M + N
        if L % 2 == 1:
            return nums[L // 2]
        else:
            return (nums[L // 2] + nums[L // 2 - 1]) / 2

    # TODO: log(M + N)
    def AC_findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pass


if __name__ == '__main__':
    pass
