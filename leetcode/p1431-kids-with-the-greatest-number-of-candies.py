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
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        curr_max = max(candies)
        res = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= curr_max:
                res.append(True)
            else:
                res.append(False)
        return res


if __name__ == '__main__':
    pass
