#!/usr/bin/env python3

import math
from collections import defaultdict
from typing import List
from typing import Set
try:
    from _tree import *
except ImportError:
    pass


class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        even = 0
        odd = 0
        for idx in chips:
            if idx % 2 == 0:
                even += 1
            else:
                odd += 1

        return min(even, odd)



if __name__ == '__main__':
    assert Solution().minCostToMoveChips([1,2,3]) == 1
    assert Solution().minCostToMoveChips([2,2,2,3,3]) == 2
