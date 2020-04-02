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
    def numTeams(self, rating: List[int]) -> int:
        size = len(rating)
        if size <= 2:
            return 0
        res = 0
        for i in range(size-2):
            for j in range(i+1, size-1):
                if rating[i] < rating[j]:
                    for k in range(j+1, size):
                        if rating[j] < rating[k]:
                            res += 1
                else:
                    for k in range(j+1, size):
                        if rating[j] > rating[k]:
                            res += 1

        return res



if __name__ == '__main__':
    pass
