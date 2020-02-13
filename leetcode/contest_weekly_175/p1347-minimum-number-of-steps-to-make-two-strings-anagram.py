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
    def minSteps(self, s: str, t: str) -> int:
        source = [0] * 26
        target = [0] * 26
        for c in s:
            idx = ord(c) - ord('a')
            source[idx] += 1

        for c in t:
            idx = ord(c) - ord('a')
            target[idx] += 1

        res = 0
        for i in range(26):
            if target[i] > source[i]:
                res += target[i] - source[i]

        return res



if __name__ == '__main__':
    pass
