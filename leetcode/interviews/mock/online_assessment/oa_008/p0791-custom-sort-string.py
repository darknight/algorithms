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
    def customSortString(self, S: str, T: str) -> str:
        size = len(S)
        if size == 0:
            return T
        cnt = Counter(T)
        res = []
        for ch in S:
            if cnt[ch] > 0:
                res.append(ch * cnt[ch])
                del cnt[ch]

        for (k, v) in cnt.items():
            res.append(k * v)

        return ''.join(res)


if __name__ == '__main__':
    Solution().customSortString("cba", "abcd")
