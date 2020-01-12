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
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        size = len(nums)
        res = []
        for i in range(0, size, 2):
            tmp = [nums[i+1]] * nums[i]
            res.extend(tmp)

        return res

if __name__ == '__main__':
    pass
