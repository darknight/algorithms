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
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        res = []
        M = len(matrix)
        N = len(matrix[0])
        for i in range(M):
            row = matrix[i]
            tmp_min = min(row)
            idx = row.index(tmp_min)
            col = []
            for ii in range(M):
                col.append(matrix[ii][idx])
            tmp_max = max(col)
            if tmp_min == tmp_max:
                res.append(tmp_min)

        return res


if __name__ == '__main__':
    pass
