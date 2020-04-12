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
    def AC_numSteps(self, s: str) -> int:
        num = 0
        size = len(s)
        for i in range(size):
            num += int(s[i]) << (size-1-i)

        res = 0
        while num != 1:
            if num % 2 == 0:
                num = num >> 1
            else:
                num += 1
            res += 1

        return res


    # TODO
    def AC_numSteps(self, s: str) -> int:
        pass

if __name__ == '__main__':
    assert Solution().numSteps("1101") == 6
