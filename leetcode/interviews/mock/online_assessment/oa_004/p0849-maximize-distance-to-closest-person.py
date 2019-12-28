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
    from _list import *
except ImportError:
    pass

try:
    from _uitl import *
except ImportError:
    pass


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        size = len(seats)
        if size == 1:
            return 0
        if size == 2:
            return 1
        sit = []
        for i in range(size):
            if seats[i] == 1:
                sit.append(i)

        res = max(sit[0] - 0, size - 1 - sit[-1])
        for i in range(0, len(sit) - 1):
            l = sit[i]
            h = sit[i + 1]
            empty = h - l - 1
            dist = (empty + 1) // 2
            res = max(res, dist)

        return res


if __name__ == '__main__':
    assert Solution().maxDistToClosest([1, 0, 0, 0, 1, 0, 1]) == 2
    assert Solution().maxDistToClosest([1, 0, 0, 0]) == 3
    assert Solution().maxDistToClosest([0, 0, 0, 0, 1, 0, 0]) == 4
    assert Solution().maxDistToClosest([0, 1, 1, 0, 1, 1, 0, 1]) == 1
