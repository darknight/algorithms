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
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] < 0:
                    res += 1

        return res


if __name__ == '__main__':
    pass
