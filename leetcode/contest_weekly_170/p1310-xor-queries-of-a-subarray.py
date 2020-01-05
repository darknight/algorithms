#!/usr/bin/env python3

import math, itertools
from collections import defaultdict, Counter
from typing import List, Set

try:
    from _tree import *
    from _list import *
    from _util import *
except ImportError:
    pass


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        """
        f(i, j) = f(0, j) ^ f(0, i-1)
        """
        size = len(arr)
        # WA for: [16] [[0,0], [0,0], [0,0]]
        # if size == 1:
        #     return arr
        for i in range(1, size):
            arr[i] = arr[i] ^ arr[i - 1]

        res = []
        for query in queries:
            l, r = query[0], query[1]
            if l == 0:
                res.append(arr[r])
            else:
                res.append(arr[r] ^ arr[l - 1])

        return res


if __name__ == '__main__':
    assert Solution().xorQueries(arr=[1, 3, 4, 8], queries=[[0, 1], [1, 2], [0, 3], [3, 3]]) == [2, 7, 14, 8]
    assert Solution().xorQueries(arr=[4, 8, 2, 10], queries=[[2, 3], [1, 3], [0, 0], [0, 3]]) == [8, 0, 4, 4]
