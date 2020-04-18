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
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        res = []
        target = list(range(1, m+1))
        for q in queries:
            pos = target.index(q)
            res.append(pos)
            target.remove(q)
            target.insert(0, q)

        return res



if __name__ == '__main__':
    pass
