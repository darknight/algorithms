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
    def AC_sortByBits(self, arr: List[int]) -> List[int]:
        bucket = []
        for _ in range(16):
            bucket.append([])

        for num in arr:
            idx = self.bits_num(num)
            bucket[idx].append(num)

        res = []
        for seg in bucket:
            res.extend(sorted(seg))

        return res


    def bits_num(self, num: int) -> int:
        res = 0
        while num > 0:
            res += num % 2
            num = num // 2

        return res


    def sortByBits(self, arr: List[int]) -> List[int]:
        """
        refer to
        https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/discuss/516999/Python-1-line
        """
        return sorted(arr, key=lambda num: (sum((num >> i) & 1 for i in range(32)), num))


if __name__ == '__main__':
    print(Solution().sortByBits([0,1,2,3,4,5,6,7,8]))
