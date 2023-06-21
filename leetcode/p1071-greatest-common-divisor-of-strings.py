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
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        size1 = len(str1)
        size2 = len(str2)
        res = ""
        for end in range(size2, 0, -1):
            t = str2[:end]
            if size2 % len(t) != 0 or size1 % len(t) != 0:
                continue
            m = t * (size1 // len(t))
            if m != str1:
                continue
            m = t * (size2 // len(t))
            if m != str2:
                continue
            res = t
            break
        return res

    # TODO
    def gcdOfStrings_official(self, str1: str, str2: str) -> str:
        pass


if __name__ == '__main__':
    print(Solution().gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX","TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))
