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
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        size = len(arr)
        total = sum(arr[:k])
        res = 0
        if total / k >= threshold:
            res += 1
        for i in range(1, size-k+1): # How to quickly identify?
            j = i + k - 1            # so troublesome
            total = total - arr[i-1] + arr[j]
            if total / k >= threshold:
                res += 1

        return res



if __name__ == '__main__':
    pass
