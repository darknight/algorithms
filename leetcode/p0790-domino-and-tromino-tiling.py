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
    def numTilings_official(self, n: int) -> int:
        """
        f(k) = f(k-1) + f(k-2) + 2 * p(k-1)
        p(k) = p(k-1) + f(k-2)
        """
        if n <= 2:
            return n

        MOD = 10 ** 9 + 7

        f = [0] * (n + 1)
        p = [0] * (n + 1)
        f[1] = 1
        f[2] = 2
        p[2] = 1

        for k in range(3, n+1):
            f[k] = (f[k-1] + f[k-2] + 2 * p[k-1]) % MOD
            p[k] = (p[k-1] + f[k-2]) % MOD

        return f[n]


if __name__ == '__main__':
    pass
