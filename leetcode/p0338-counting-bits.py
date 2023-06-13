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
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        res = [0] * (n + 1)
        res[0] = 0
        res[1] = 1
        pow = 2
        while pow <= n:
            res[pow] = 1 # 2, 4, 8, 16, 32, ...
            k = 1
            while k < pow and k + pow <= n:
                res[pow+k] = 1 + res[k]
                k += 1
            pow = pow * 2

        return res

    def countBits_official_3(self, n: int) -> List[int]:
        """
        DP - 1D
        P(x) = P(x/2) + (x mod 2)
        """
        res = [0] * (n + 1)
        for x in range(1, n+1):
            # x >> 1 == x // 2
            # x & 1 == x % 2
            res[x] = res[x >> 1] + (x & 1)
        return res

    def countBits_official_4(self, n: int) -> List[int]:
        """
        DP - 1D
        P(x) = P(x & (x-1)) + 1
        """
        res = [0] * (n + 1)
        for x in range(1, n+1):
            res[x] = res[x & (x-1)] + 1
        return res


if __name__ == '__main__':
    print(Solution().countBits(2))
    print(Solution().countBits(5))
