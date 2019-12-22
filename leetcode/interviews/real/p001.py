#!/usr/bin/env python3

import math
from collections import defaultdict
from typing import List
from typing import Set
try:
    from _tree import *
except ImportError:
    pass

try:
    from _uitl import *
except ImportError:
    pass

class Solution:
    """
    merge a sorted list of integers into range string
    """
    def find_range(self, arr: List[int]) -> str:
        size = len(arr)
        if size == 0:
            return ""
        if size == 1:
            return str(arr[0])

        p = 0
        res = []
        while p < size:
            q = p + 1
            while q < size:
                if arr[q] - arr[q - 1] == 1:
                    q += 1
                else:
                    break
            if q - p == 1:
                res.append(str(arr[p]))
            else:
                res.append("%d-%d" % (arr[p], arr[q - 1]))
            p = q

        return ",".join(res)


if __name__ == '__main__':
    res = Solution().find_range([1,2,3,4,6,9,10,13,14,15,18,20,21])
    assert res == "1-4,6,9-10,13-15,18,20-21"

    res = Solution().find_range([18, 20, 23])
    assert res == "18,20,23"
