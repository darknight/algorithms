#!/usr/bin/env python3

import math
import itertools
from collections import defaultdict
from typing import List
from typing import Set
try:
    from _tree import *
except ImportError:
    pass

try:
    from _list import *
except ImportError:
    pass

try:
    from _uitl import *
except ImportError:
    pass


class Solution:
    def AC_findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        size = len(arr)

        prefix = 0
        sums = []
        for i in range(size):
            sums.append(prefix + arr[i] * (size - i))
            prefix += arr[i]

        if target >= sums[-1]:
            return arr[-1]

        t = -1
        i = 0
        while sums[i] < target:
            t = i
            i += 1

        if t == -1:
            l = 1
            lsum = 1 * size
            h = arr[0]
            hsum = sums[0]
        else:
            l = t
            lsum = sums[t]
            h = arr[t + 1]
            hsum = sums[t + 1]

        res = self.bin_search(l, h, lsum, hsum, target, size-i)

        return res

    def bin_search(self, low, high, lsum, hsum, target, multiple) -> int:
        l = low
        h = high
        while l <= h:
            mid = l + (h - l) // 2
            msum = hsum - (high-mid) * multiple
            if msum == target:
                return mid
            if msum < target:
                l = mid + 1
            else:
                h = mid - 1

        m1 = hsum - (high - l) * multiple
        m2 = hsum - (high - (l - 1)) * multiple
        if abs(m2-target) <= abs(m1-target):
            return l - 1

        return l

    # TODO:
    def findBestValue(self, arr: List[int], target: int) -> int:
        """

        """
        pass


if __name__ == '__main__':
    assert Solution().findBestValue(arr = [4,9,3], target = 10) == 3
    # assert Solution().findBestValue(arr = [2,3,5], target = 10) == 5
    # assert Solution().findBestValue(arr = [60864,25176,27249,21296,20204],
    #                                 target = 56803) == 11361
    # assert Solution().findBestValue([48772,52931,14253,32289,75263],40876) == 8175