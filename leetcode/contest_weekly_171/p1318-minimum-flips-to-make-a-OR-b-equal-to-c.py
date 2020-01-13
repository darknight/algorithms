#!/usr/bin/env python3

import math, itertools
from collections import defaultdict, Counter
from typing import List, Set
try:
    from _tree import *
    from _list import *
    from _util import *
except ImportError:
    pass

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        while c > 0:
            la = a % 2
            lb = b % 2
            lc = c % 2
            if lc == 1:
                if la == 0 and lb == 0:
                    res += 1
            else:
                if la == 1 and lb == 1:
                    res += 2
                elif la == 1 or lb == 1:
                    res += 1
            a = a >> 1
            b = b >> 1
            c = c >> 1

        while a > 0:
            res += a % 2
            a = a >> 1

        while b > 0:
            res += b % 2
            b = b >> 1

        return res

if __name__ == '__main__':
    pass
