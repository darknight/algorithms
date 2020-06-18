#!/usr/bin/env python3

import math, itertools, functools, heapq, re
from collections import defaultdict, Counter
from typing import List, Set, Dict, Tuple
try:
    from _tree import *
    from _list import *
    from _util import *
except ImportError:
    pass


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        c = 0
        r = 0
        o = 0
        a = 0
        total = 0
        for ch in croakOfFrogs:
            if c < 0 or r < 0 or o < 0 or a < 0:
                return -1
            if ch == 'c':
                c += 1
            elif ch == 'r':
                c -= 1
                r += 1
            elif ch == 'o':
                r -= 1
                o += 1
            elif ch == 'a':
                o -= 1
                a += 1
            elif ch == 'k':
                total = max(total, c + r + o + a)
                a -= 1
            else:
                return -1

        if c + r + o + a != 0:
            return -1
        return total


if __name__ == '__main__':
    pass
