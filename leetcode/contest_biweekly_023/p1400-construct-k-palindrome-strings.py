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
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        cnt = [0] * 26
        for c in s:
            idx = ord(c) - ord('a')
            cnt[idx] += 1

        even, odd = 0, 0
        for val in cnt:
            if val == 0:
                continue
            if val % 2 == 1:
                odd += 1
            else:
                even += 1

        if odd > k:
            return False

        return True



if __name__ == '__main__':
    pass
