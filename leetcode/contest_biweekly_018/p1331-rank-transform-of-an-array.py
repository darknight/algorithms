#!/usr/bin/env python3

import math, itertools
from collections import defaultdict, Counter
from typing import List, Set, Dict, Tuple
try:
    from _tree import *
    from _list import *
    from _util import *
except ImportError:
    pass

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        size = len(arr)
        if size == 0:
            return []
        sarr = sorted(arr)
        rank = 1
        rank_map = { sarr[0]: rank }
        for i in range(1, size):
            if sarr[i] == sarr[i-1]:
                continue
            rank += 1
            rank_map[sarr[i]] = rank
        res = []
        for num in arr:
            res.append(rank_map[num])

        return res



if __name__ == '__main__':
    pass
