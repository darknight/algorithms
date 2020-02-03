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
    def minSetSize(self, arr: List[int]) -> int:
        size = len(arr)
        target = size // 2
        cnt = defaultdict(int)
        for num in arr:
            cnt[num] += 1

        counts = sorted(cnt.values(), reverse=True)
        res = 0
        while size > target:
            size -= counts[res]
            res += 1

        return res




if __name__ == '__main__':
    assert Solution().minSetSize([3,3,3,3,5,5,5,2,2,7]) == 2
