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
    def countLargestGroup(self, n: int) -> int:
        cnt = defaultdict(int)
        size = 0
        for num in range(1, n+1):
            dig_sum = 0
            while num > 0:
                dig_sum += num % 10
                num = num // 10
            cnt[dig_sum] += 1
            size = max(size, cnt[dig_sum])

        res = 0
        for val in cnt.values():
            if val == size:
                res += 1

        return res



if __name__ == '__main__':
    pass
