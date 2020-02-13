#!/usr/bin/env python3

import math, itertools, functools
from collections import defaultdict, Counter
from typing import List, Set, Dict, Tuple
try:
    from _tree import *
    from _list import *
    from _util import *
except ImportError:
    pass

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        nums = []
        M = len(mat)
        idx_map = defaultdict(list)
        for i in range(M):
            n = sum(mat[i])
            idx_map[n].append(i)
            nums.append(n)

        nums.sort()
        res = []
        i = 0
        while i < k:
            n = nums[i]
            for idx in idx_map[n]:
                res.append(idx)
                i += 1

        return res[:k]


if __name__ == '__main__':
    pass
