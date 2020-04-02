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
    def getKth(self, lo: int, hi: int, k: int) -> int:

        @functools.lru_cache(None)
        def get_power(n: int) -> int:
            if n == 1:
                return 0
            if n == 2:
                return 1
            if n % 2 == 0:
                return get_power(n // 2) + 1
            else:
                return get_power(3 * n + 1) + 1

        cache = [0] * 1024
        for i in range(1, 1001):
            cache[i] = get_power(i)

        pairs = []
        for num in range(lo, hi+1):
            pairs.append((cache[num], num))

        pairs.sort()
        return pairs[k-1][-1]



if __name__ == '__main__':
    assert Solution().getKth(lo = 7, hi = 11, k = 4) == 7
