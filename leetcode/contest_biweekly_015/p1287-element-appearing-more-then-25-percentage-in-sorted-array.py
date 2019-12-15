#!/usr/bin/env python3

import math
import itertools
from collections import defaultdict
from typing import List
from typing import Set
try:
    from _tree import *
except ImportError:
    pass

try:
    from _uitl import *
except ImportError:
    pass


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        size = len(arr)
        target = size * 0.25
        cnt = defaultdict(int)
        for n in arr:
            cnt[n] += 1
            if cnt[n] > target:
                return n


if __name__ == '__main__':
    assert Solution().findSpecialInteger([1,2,2,6,6,6,6,7,10]) == 6
