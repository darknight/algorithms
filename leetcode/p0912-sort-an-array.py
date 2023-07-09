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
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort_1(nums, 0, len(nums) - 1)
        return nums

    def quick_sort_1(self, arr: List[int], start: int, end: int):
        if start >= end:
            return
        # partition
        pivot = arr[end]
        i = start
        for j in range(start, end):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[end] = arr[end], arr[i]
        # recursive
        self.quick_sort_1(arr, start, i-1)
        self.quick_sort_1(arr, i+1, end)


if __name__ == '__main__':
    pass
