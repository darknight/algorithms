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
    def minStartValue(self, nums: List[int]) -> int:
        s = 0
        res = 0
        for n in nums:
            s += n
            res = min(res, s)
        if res >= 0:
            return 1
        else:
            return abs(res-1)


if __name__ == '__main__':
    pass
