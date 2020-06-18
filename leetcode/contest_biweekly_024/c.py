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
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        def perm(prefix: str, i: int):
            if i == n:
                res.append(prefix)
                return
            last_ch = prefix[-1]
            if last_ch == 'a':
                perm(prefix+'b', i+1)
                perm(prefix+'c', i+1)
            elif last_ch == 'b':
                perm(prefix + 'a', i + 1)
                perm(prefix + 'c', i + 1)
            else:
                perm(prefix + 'a', i + 1)
                perm(prefix + 'b', i + 1)

        perm('a', 1)
        perm('b', 1)
        perm('c', 1)

        res.sort()

        if len(res) < k:
            return ''
        return res[k-1]


if __name__ == '__main__':
    assert Solution().getHappyString(1,3) == 'c'
    assert Solution().getHappyString(1,4) == ''
    assert Solution().getHappyString(3,9) == 'cab'
    assert Solution().getHappyString(2,7) == ''
    assert Solution().getHappyString(10,100) == 'abacbabacb'
