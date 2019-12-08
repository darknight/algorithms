#!/usr/bin/env python3

import math
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
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        bucket = defaultdict(list)
        for (i, group) in enumerate(groupSizes):
            bucket[group].append(i)

        res = []
        for (k, v) in bucket.items():
            while len(v) > 0:
                tmp = v[:k]
                v = v[k:]
                res.append(tmp)

        return res



if __name__ == '__main__':
    Solution().groupThePeople(groupSizes = [3,3,3,3,3,1,3])
    Solution().groupThePeople(groupSizes = [2,1,3,3,3,2])
