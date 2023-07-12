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
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        curr = 0
        for g in gain:
            curr += g
            highest = max(highest, curr)

        return highest



if __name__ == '__main__':
    pass
