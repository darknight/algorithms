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
    def numTimesAllBlue(self, light: List[int]) -> int:
        on = [1] + [0] * len(light)
        yellow = 0
        prefix = 0
        res = 0
        for idx in light:
            on[idx] = 1
            yellow += 1
            if idx - 1 == prefix:
                while prefix < len(light) and on[prefix+1] == 1:
                    prefix += 1
                    yellow -= 1
                if yellow == 0:
                    res += 1

        return res



if __name__ == '__main__':
    assert Solution().numTimesAllBlue([2,1,3,5,4]) == 3
    assert Solution().numTimesAllBlue([4,1,2,3]) == 1
